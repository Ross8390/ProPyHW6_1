ids = {'user1': [213, 213, 213, 15, 213],
     'user2': [54, 54, 119, 119, 119],
     'user3': [213, 98, 98, 35]}


def dictionary_filter(object: dict) -> list:
    object_set = set()
    for i in ids.values():
        object_set.update(i)
    return list(object_set)



if __name__ == '__main__':

     my_list = dictionary_filter(ids)
     print(my_list)