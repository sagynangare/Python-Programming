import pickle

example_dict = {1:"5",2:"3",3:"f"}

pickle_out = open("dict.pickle","wb")
pickle.dump(example_dict,pickle)
pickle_out.close()
