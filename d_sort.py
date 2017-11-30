import MapReduce

def mapper(key, value):
    key = 0
    sorted_list = []
    for a in value:
        sorted_list.append(a)
        mr.emit_intermediate(key,(a))

def reducer(key, list_of_values):
    mr.emit(sorted((list_of_values)))

# ____________________________________________________________________________
# This code remains unmodified in all programs, except for the input file name.

if __name__ == '__main__':
    data = open("integers.json")
    mr = MapReduce.MapReduce()
    mr.execute(data, mapper, reducer)