'''Quick and dirty script to generate directory structure from PDF TOC'''
import os
import re

from anytree import Node, RenderTree, find

FILENAME = "toc2.txt"
ROOT = Node(".", parent=None)


def get_prefix(line):
    '''Get the prefix of the line'''
    match = re.search(r"^([0-9]+(\.[0-9]+)*)", line)
    if match:
        prefix = match.group(1)
        return prefix
    else:
        print("No match found")
        exit(1)


def get_parent_prefix(prefix):
    '''Get the parent prefix of the line'''
    return '.'.join(prefix.rsplit('.')[:-1])


def find_node(line):
    '''Find the node of the line'''
    return find(ROOT, lambda node: node.name == line)


def find_parent(line):
    '''Find the parent of the line'''
    prefix = get_prefix(line)
    parent_prefix = get_parent_prefix(prefix)
    print(parent_prefix)
    res = ROOT
    if parent_prefix == '':
        return res

    with open(FILENAME, "r", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            l_n = line.strip()
            if l_n.startswith(parent_prefix):
                tmp = find_node(l_n)
                if tmp:
                    res = tmp
                    break
                else:
                    print(f"no node found for {l_n}")
                    res = ROOT
                    break

    return res


def main():
    '''Main function'''
    # open the file
    with open(FILENAME, "r", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            l_n = line.strip()
            print(f"finding parent of {l_n}")
            parent = find_parent(l_n)
            print(f"parent is {parent}")
            Node(l_n, parent=parent)

    for pre, _, node in RenderTree(ROOT):
        print(f"{pre}{node.name}")

    # Use RenderTree to visualize the tree structure
    rtree = RenderTree(ROOT)

    # Create the directories according to the tree structure
    for _, _, node in rtree:
        path = os.path.join(*[p.name for p in node.path])
        if not os.path.exists(path):
            os.makedirs(path)


if __name__ == "__main__":
    main()
