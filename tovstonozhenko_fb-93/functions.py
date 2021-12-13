from re import match


def incorrect_name(set_name: str):
    if match(r"^[a-zA-Z][a-zA-Z0-9_]*$", set_name): return False
    return True


def incorrect_coordinates(coordinates: str):
    coordinates = "".join(coordinates.split())
    if match(r"^[(][0-9][,][0-9][)]$", coordinates): return False
    return True


def create(set_name: str):
    if len(set_name.split()) > 1:
        print("expected one word in the set name (" + str(len(set_name.split())) + " words given)")
    else:
        if incorrect_name(set_name): print("incorrect set name")
        else:
            #print("create was called")
            #
            print("set " + set_name + " has been created")


def insert(point: str):
    if incorrect_name(point.split()[0]): print("incorrect set name")
    elif incorrect_coordinates(point[len(point.split()[0]) + 1:]): print("incorrect point coordinates")
    #elif point.split()[0] not in     :
        #print("set name " + point.split()[0] + " does not exist")
    else:
        #print("insert was called")
        #
        print("point " + "".join(point[len(point.split()[0])+1:].split()) + " has been added to " + point.split()[0])


def print_tree(tree_name: str):
    if incorrect_name(tree_name): print("incorrect tree name")
    #elif tree_name not in     :
        #print("tree name " + point.split()[0] + " does not exist")
    else:
        print("print_tree was called")
        #



def contains(point: str):
    if incorrect_name(point.split()[0]): print("incorrect set name")
    elif incorrect_coordinates(point[len(point.split()[0]) + 1:]): print("incorrect point coordinates")
    # elif point.split()[0] in     : return True
    else:
        return False



def search(set_name: str):
    if incorrect_name(set_name.split()[0]): print("incorrect set name")
    #elif set_name not in     :
        #print("set name " + point.split()[0] + " does not exist")
    else:
        print("search was called")
        if (len(set_name.split()) == 2): print ("incorrect command syntax")
        if (len(set_name.split()) > 2):
            if set_name.split()[1].lower() == "where":
                condition_params = set_name[
                                   len(set_name.split()[0]) + len(set_name.split()[1]) + len(set_name.split()[2]) + 3:]
                if set_name.split()[2].lower() == "inside": where_inside(condition_params)
                elif set_name.split()[2].lower() == "above_to": where_above_to(condition_params)
                elif set_name.split()[2].lower() == "nn": where_nearest_neighbour(condition_params)
                else: print("incorrect condition syntax")
            else: print("incorrect command syntax")
        #else:


def where_inside(coordinates: str):
    coordinates = "".join(coordinates.split())
    if not match(r"^[(][0-9][,][0-9][)][,][(][0-9][,][0-9][)]$", coordinates): print("incorrect point coordinates")
    else:
        print("where inside was called")
        #


def where_above_to(coordinate: str):
    if not coordinate.isdigit(): print("incorrect coordinate")
    else:
        print("where above to was called")
        #


def where_nearest_neighbour(point: str):
    if incorrect_coordinates(point): print("incorrect point coordinates")
    else:
        print("where nearest neighbour was called")
        #


def exit():
    print("exit was called")