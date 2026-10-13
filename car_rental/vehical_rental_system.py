
from typing import List

from car_rental.store import Store
from car_rental.user import User

class VehicleRentalSystem:
    def __init__(self):
        self.store_list: List[Store] = []
        self.user_list: List[User] = []

    def get_store(self, store_id: int) -> Store:
        store = next((s for s in self.store_list if s.store_id == store_id), None)

        if store is None:
            raise ValueError(f"Store with {store_id} not found in system...")

        return store

    def get_user(self, user_id: int) -> User:
        user = next((u for u in self.user_list if u.user_id == user_id), None)

        if user is None:
            raise ValueError(f"User with {user_id} not found in system...")

        return user

    def add_store(self, store: Store) -> None:
        self.store_list.append(store)

    def add_user(self, user: User) -> None:
        self.user_list.append(user)

    def remove_store(self, store_id: int) -> None:
        store = next((s for s in self.store_list if s.store_id == store_id), None)
        if store is not None:
            self.store_list.remove(store)

    def remove_user(self, user_id: int) -> None:
        user = next((u for u in self.user_list if u.user_id == user_id), None)
        if user is not None:
            self.user_list.remove(user)