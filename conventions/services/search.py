from abc import ABC, abstractmethod
from typing import List, Sequence

from django.conf import settings
from django.db.models import QuerySet
from django.core.paginator import Paginator

from bailleurs.models import Bailleur
from conventions.models import Convention, ConventionStatut
from instructeurs.models import Administration
from programmes.models import Programme, Financement
from users.models import User


class ConventionSearchBaseService(ABC):
    @abstractmethod
    def get_base_query_set(self) -> QuerySet:
        pass

    def get_order_by_fields(self) -> List:
        return ["cree_le"]

    def get_query_set(self) -> QuerySet:
        return self.get_base_query_set().order_by(*self.get_order_by_fields())

    def get_total(self) -> int:
        """
        Return the total number of lines targeted by the base query, without filters
        """
        return self.get_query_set().count()

    def get_results(
        self, page: int = 1, size: int | None = None
    ) -> Sequence[Convention]:
        """
        Return the paginated list of matched conventions
        """
        return Paginator(
            self.get_query_set(), size or settings.APILOS_PAGINATION_PER_PAGE
        ).get_page(page)


class AvenantListSearchService(ConventionSearchBaseService):
    def __init__(self, convention: Convention, order_by_numero: bool = False):
        self.convention: convention = (
            convention.parent if convention.is_avenant() else convention
        )
        self.order_by_numero: bool = order_by_numero

    def get_order_by_fields(self) -> List:
        return ["numero"] if self.order_by_numero else super().get_order_by_fields()

    def get_base_query_set(self) -> QuerySet:
        return (
            self.convention.avenants.all()
            .prefetch_related("programme")
            .prefetch_related("lot")
        )


class ProgrammeConventionSearchService(ConventionSearchBaseService):
    def __init__(self, programme: Programme, order_by: str | None = None):
        self.programme: programme
        self.order_by: str | None = order_by

    def get_base_query_set(self) -> QuerySet:
        return (
            Convention.objects.filter(programme=self.programme)
            .prefetch_related("programme")
            .prefetch_related("programme__administration")
            .prefetch_related("lot")
        )

    def get_order_by_fields(self) -> List:
        return [self.order_by] if self.order_by is not None else []


class UserConventionSearchService(ConventionSearchBaseService):
    def __init__(
        self,
        user: User,
        statuses: List[ConventionStatut],
        order_by: str | None = None,
        statut: str | None = None,
        financement: str | None = None,
        departement: str | None = None,
        commune: str | None = None,
        search_input: str | None = None,
        anru: bool = False,
        bailleur: Bailleur | None = None,
        administration: Administration | None = None,
    ):
        self.user: User = user
        self.order_by: str | None = order_by
        self.statuses = statuses
        self.statut: ConventionStatut | None = ConventionStatut.get_by_label(statut)
        self.financement: str | None = financement
        self.departement: str | None = departement
        self.commune: str | None = commune
        self.search_input: str | None = search_input
        self.anru: bool = anru
        self.bailleur: Bailleur | None = bailleur
        self.administration: Administration | None = administration

    def get_base_query_set(self) -> QuerySet:
        return (
            self.user.conventions()
            .prefetch_related("programme")
            .prefetch_related("programme__administration")
            .prefetch_related("lot")
            .filter(statut__in=map(lambda s: s.label, self.statuses))
            .filter(
                **{
                    # Application du filtre "statut de la convention"
                    **({"statut": self.statut.label} if self.statut is not None else {})
                }
            )
            # TODO appliquer les autres filtres
        )
