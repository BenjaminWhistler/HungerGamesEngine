import random
import time

class Event:
    events = {
        "Standard": 0,
        "Combat": 1,
        "Loot": 2
    }
    def __init__(self, key, event_string, event_type="Standard", hp=None, weapon_rating=None, loot=None, post_loot_string=None, loot_type=None, user_first=True, left=None, right=None, user=None):
        """Store value, left, and right. Children initially reference None."""
        # TODO: Implement this constructor.
        self.key = key
        self.event_string = event_string
        self.event_type = self.events[event_type]
        self.hp = hp
        self.weapon_rating = weapon_rating
        self.loot = loot
        self.post_loot_string = post_loot_string
        self.loot_type = loot_type
        self.user_first = user_first
        self.left = left
        self.right = right
        self.user = user

class Tribute:
    weapons = {
            "Sword": 50,
            "Axe": 90,
            "Dagger": 35,
            "Stone": 20,
            "None": 10
    }
    healing = {
        "Bandages": 20,
        "Morphling": 50,
    }
    def __init__(self, hp=100, weapon="Fists", weapon_rating=10, current_event=None):
        self.hp = hp
        self.weapon = weapon
        self.weapon_rating = weapon_rating
        self.current_event = current_event
    
    def combat(self, event_hp, event_weapon_rating, user_first=True):
        if user_first:
            time.sleep(2)
            user_attack = random.randint(self.weapon_rating // 2, self.weapon_rating * 2)
            event_hp -= user_attack
            print("\nYou did " + f"{user_attack}" + " damage!")
            if event_hp <= 0:
                return True
            print("Enemy HP Left: " + f"{event_hp}")
            time.sleep(2)
            event_attack = random.randint(event_weapon_rating // 2, event_weapon_rating * 2)
            self.hp -= event_attack
            print("\nYou took " + f"{event_attack}" + " damage!")
            if self.hp <= 0:
                return False
            else:
                print("Your HP Left: " + f"{self.hp}")
                return self.combat(event_hp, event_weapon_rating)
        else:
            time.sleep(2)
            while self.hp > 0 and event_hp > 0:
                event_attack = random.randint(event_weapon_rating // 2, event_weapon_rating * 2)
                print("\nYou took " + f"{event_attack}" + " damage!")
                self.hp -= event_attack
                if self.hp <= 0:
                    break
                print("Your HP Left: " + f"{self.hp}")
                time.sleep(2)
                user_attack = random.randint(self.weapon_rating // 2, self.weapon_rating * 2)
                event_hp -= user_attack
                print("\nYou did " + f"{user_attack}" + " damage!")
                if event_hp <= 0:
                    break
                print("Enemy HP Left: " + f"{event_hp}")
                time.sleep(2)
            if self.hp <= 0:
                return False
            else:
                return True
    def loot(self, current, loot, choice, post_loot_string, loot_type):
        if choice == "1":
            if loot_type == "Weapon":
                print("You grab the " + f"{loot}" + ".")
                self.weapon = loot
                self.weapon_rating = self.weapons[loot]
                current.event_type = "Standard"
                return post_loot_string
            elif loot_type == "Healing":
                print("You use the " + f"{loot}" + ".")
                self.hp += self.healing[loot]
                if self.hp > 100:
                    self.hp = 100
                current.event_type = "Standard"
                return post_loot_string
            else:
                return post_loot_string
        else:
            print("You leave the " + f"{loot}" + ".")
            current.event_type = "Standard"
            return post_loot_string


class BinaryTree:
    key = 0
    def __init__(self):
        """Initialize self.root to None."""
        # TODO: Implement this method. Helpers are allowed.
        self.root = None

    def set_root(self, event_string):
        """Create and return the root; raise ValueError if it exists."""
        # TODO: Implement this method. Helpers are allowed.
        if self.root is not None:
            raise ValueError("Root already exists")
        self.root = Event(self.key, event_string)
        self.key += 1
        return self.root

    def get_root(self):
        """Return the root node, or None."""
        # TODO: Implement this method. Helpers are allowed.
        return self.root

    def add_left(self, parent, event_string, event_type="Standard", hp=None, weapon=None, loot=None, post_loot_string=None, loot_type=None, user_first=True):
        """Create and return a left child; raise ValueError if occupied."""
        # TODO: Implement this method. Helpers are allowed.
        if parent.left is not None:
            raise ValueError("Left child already exists")
        parent.left = Event(self.key, event_string, event_type, hp, weapon, loot, post_loot_string, loot_type, user_first)
        self.key += 1
        return parent.left

    def add_right(self, parent, event_string, event_type="Standard", hp=None, weapon=None, loot=None, post_loot_string=None, loot_type=None, user_first=True):
        """Create and return a right child; raise ValueError if occupied."""
        # TODO: Implement this method. Helpers are allowed.
        if parent.right is not None:
            raise ValueError("Right child already exists")
        parent.right = Event(self.key, event_string, event_type, hp, weapon, loot, post_loot_string, loot_type, user_first)
        self.key += 1
        return parent.right

    def preorder(self, tree_list=None):
        """Recursively return values in root-left-right order."""
        # TODO: Implement this method. Helpers are allowed.
        if self.get_root is None:
            return None
        if tree_list is None:
            tree_list = []
        self._preorder(self.root, tree_list)
        return tree_list

    def _preorder(self, root, tree_list):
        if root is None:
            return
        print(root.event_string)
        tree_list.append(root.event_string)
        self._preorder(root.left, tree_list)
        self._preorder(root.right, tree_list)

    def inorder(self, tree_list=None):
        """Recursively return values in root-left-right order."""
        # TODO: Implement this method. Helpers are allowed.
        if self.get_root is None:
            return None
        if tree_list is None:
            tree_list = []
        self._inorder(self.root, tree_list)
        return tree_list

    def _inorder(self, root, tree_list):
        if root is None:
            return
        self._inorder(root.left, tree_list)
        print(root.event_string)
        tree_list.append(root.event_string)
        self._inorder(root.right, tree_list)

    def postorder(self, tree_list=None):
        """Recursively return values in root-left-right order."""
        # TODO: Implement this method. Helpers are allowed.
        if self.get_root is None:
            return None
        if tree_list is None:
            tree_list = []
        self._postorder(self.root, tree_list)
        return tree_list

    def _postorder(self, root, tree_list):
        if root is None:
            return
        self._postorder(root.left, tree_list)
        self._postorder(root.right, tree_list)
        print(root.event_string)
        tree_list.append(root.event_string)

    def find_path(self, target_node, path_list=None):
        """Recursively return root-to-target values, or None; match by identity."""
        # TODO: Implement this method. Helpers are allowed.
        if self.get_root is None or target_node is None:
            return None
        if path_list is None:
            path_list = []
        self._find_path(self.root, target_node, path_list)
        if path_list == []:
            raise ValueError("Invalid path!")
        path_list.reverse()
        for event in path_list:
            print(event)
        return path_list

    def _find_path(self, root, target_node, path_list):
        if root is None:
            return None
        if root is target_node:
            path_list.append(root.event_string)
            return True
        if self._find_path(root.left, target_node, path_list):
            path_list.append(root.event_string)
            return True
        if self._find_path(root.right, target_node, path_list):
            path_list.append(root.event_string)
            return True
        return None

    def count_leaves(self):
        return self._count_leaves(self.root)

    def _count_leaves(self, root):
        if root is None:
            return 0
        if (root.left is None) and (root.right is None):
            return 1
        return self._count_leaves(root.left) + self._count_leaves(root.right)

    def height(self):
        return self._height(self.root)

    def _height(self, root):
        if root is None:
            return -1
        if (root.left is None) and (root.right is None):
            return 0
        x = (1 + self._height(root.left))
        y = (1 + self._height(root.right))
        return x if x > y else y

    @staticmethod
    def navigate(current, user, choice):
        if choice == "1":
            if current.event_type == current.events["Loot"]:
                current.event_string = user.loot(current, current.loot, choice, current.post_loot_string, loot_type=current.loot_type)
                return current
            current = current.left
            if current.event_type == current.events["Combat"]:
                print(current.event_string)
                if user.combat(current.hp, current.weapon_rating, current.user_first):
                    if current.left:
                        return current.left
                    else:
                        raise AttributeError("Please add a left child!")
                else:
                    if current.right:
                        return current.right
                    else:
                        raise AttributeError("Please add a right child!")
            else:
                return current
        elif choice == "2":
            current = current.right
            if current.event_type == current.events["Combat"]:
                print(current.event_string)
                if user.combat(current.hp, current.weapon_rating, current.user_first):
                    if current.left:
                        return current.left
                    else:
                        raise AttributeError("Please add a left child!")
                else:
                    if current.right:
                        return current.right
                    else:
                        raise AttributeError("Please add a right child!")
            else:
                return current
        if choice == "3":
            print("\nTribute stats:\n" + f"Health: {user.hp}" + "\n" + f"Weapon: {user.weapon}" + "\n" + f"Weapon rating: {user.weapon_rating}\n")
            return current
        else:
            print("\nInvalid choice, try again\n")
            return current

