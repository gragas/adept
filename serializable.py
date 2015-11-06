import json

class Serializable: #Converts objects into strings and vice versa

        #Anything that needs to be saved should extend this or extend something that extends this

        def serialize(self): #Gives the object encoded as a string
                return json.dumps(self, default=Serializable.to_default_type)

        @staticmethod
        def deserialize(s): #Gives the string decoded as an object
                return json.loads(s, object_hook=Serializable.to_object)

        @staticmethod
        def to_default_type(obj): #Converts the object into a dictionary so it can be json encoded
                try:
                        d = { '__class__':obj.__class__.__name__, 
                                '__module__':obj.__module__,
                                }
                        d.update(obj.__dict__)
                        return d
                except (AttributeError):
                        return None

        @staticmethod
        def to_object(d): #Takes a dictionary (Presumably one that was encoded as per above) and uses it to create an object
                if not "__class__" in d.keys():
                        return d
                class_name = d.pop("__class__")
                module_name = d.pop('__module__')
                module = __import__(module_name)
                class_ = getattr(module, class_name)
                args = dict((key, value) for key, value in d.items())
                inst = class_(**args)
                return inst
