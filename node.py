from dataclasses import dataclass


@dataclass
class SinglyNode:
    value: object = None
    node_next: 'SinglyNode' = None
    is_head: bool = False
    is_tail: bool = False


@dataclass
class DoublyNode:
    value: object = None
    node_next: 'DoublyNode' = None
    node_prev: 'DoublyNode' = None
    is_head: bool = False
    is_tail: bool = False


@dataclass
class TreeNode:
    value: object
    node_LHS: 'TreeNode' = None
    node_RHS: 'TreeNode' = None
    node_parent: 'TreeNode' = None
