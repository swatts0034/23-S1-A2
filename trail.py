from __future__ import annotations
from dataclasses import dataclass

from mountain import Mountain
from data_structures.stack_adt import ArrayStack

from typing import TYPE_CHECKING, Union

# Avoid circular imports for typing.
if TYPE_CHECKING:
    from personality import WalkerPersonality

@dataclass
class TrailSplit:
    """
    A split in the trail.
       ___path_top____
      /               \
    -<                 >-path_follow-
      \__path_bottom__/
    """

    path_top: Trail
    path_bottom: Trail
    path_follow: Trail

    def remove_branch(self) -> TrailStore:
        """Removes the branch, should just leave the remaining following trail.
        Parameters: None
        Returns: TrailStore ojbect
        """

        # Remove the top and bottom branch, so just return follow_path.store
        return self.path_follow.store

@dataclass
class TrailSeries:
    """
    A mountain, followed by the rest of the trail

    --mountain--following--

    """

    mountain: Mountain
    following: Trail

    def remove_mountain(self) -> TrailStore:
        """Removes the mountain at the beginning of this series."""
        raise NotImplementedError()


    def add_mountain_before(self, mountain: Mountain) -> TrailStore:
        """Adds a mountain in series before the current one.
        Parameters: mountain, A mountain object to add to the series
        Return: TrailSeries
        """
        # Create a new Trail series with the passed in mountain, and make the existing mountain and following into a new TrailSeries that follows
        # Could this just be TrailSeries(mountain, Trail(self)) ???
        return TrailSeries(mountain, Trail(TrailSeries(self.mountain, self.following)))

    def add_empty_branch_before(self) -> TrailStore:
        """Adds an empty branch, where the current trailstore is now the following path.

        Parameters: None
        Return: TrailSplit

        """

        return = TrailSplit(Trail(None), Trail(None), Trail(self))



    def add_mountain_after(self, mountain: Mountain) -> TrailStore:
        """Adds a mountain after the current mountain, but before the following trail.

        Parameters: mountain, the mountain to add
        Returns: Trailstore object

        """

        # Create a new series with the new mountain and existing following traio
        following_series = Trail(TrailSeries(mountain, self.following))

        # return a new series with the existing mountain and the following series
        return TrailSeries(self.mountain, following_series)


    def add_empty_branch_after(self) -> TrailStore:
        """
        Adds an empty branch after the current mountain, but before the following trail.
        Parameters: None
        Return: The modified TrailSeries object
        """
        # create a new split, top and bottom are none, and following becomes the new following part
        new_split = Trail(TrailSplit(Trail(None), Trail(None), self.following))

        # Put the split into a series along with the mountain
        return = TrailSeries(self.mountain, new_split)


TrailStore = Union[TrailSplit, TrailSeries, None]

@dataclass
class Trail:

    store: TrailStore = None

    def add_mountain_before(self, mountain: Mountain) -> Trail:
        """Adds a mountain before everything currently in the trail."""
        # Create a new trail series,
        if self.store is not None:
            new_trail_series = Trail(TrailSeries(mountain, self.store.following))
        else:
            new_trail_series = Trail(TrailSeries(mountain, Trail(None)))

        return new_trail_series

    def add_empty_branch_before(self) -> Trail:
        """Adds an empty branch before everything currently in the trail."""
        if self.store is not None:
            new_trail_split = Trail(TrailSplit(Trail(None), Trail(None),self.store.following))
        else:
            new_trail_split = Trail(TrailSplit(Trail(None), Trail(None), Trail(None)))

        return new_trail_split

    def follow_path(self, personality: WalkerPersonality) -> None:
        """Follow a path and add mountains according to a personality."""
        raise NotImplementedError()


    def collect_all_mountains(self) -> list[Mountain]:
        """Returns a list of all mountains on the trail."""
        raise NotImplementedError()

    def length_k_paths(self, k) -> list[list[Mountain]]: # Input to this should not exceed k > 50, at most 5 branches.
        """
        Returns a list of all paths of containing exactly k mountains.
        Paths are represented as lists of mountains.

        Paths are unique if they take a different branch, even if this results in the same set of mountains.
        """
        raise NotImplementedError()
