""" JSON (Javascript Object Notation) is a lightweight data-interchange format
    JSON is built on two structures:
      * A collection of name/value pairs (e.g. an object, record, dic, table, etc)
      * An ordered list of values (e.g. an array, vector, list, or sequence)

      An object is an unordered set of name/value pairs.  An object begins with
      { left brace and ends with right brace }.  Each name is followed by : (color)
      and the name/value pairs are separated by , (comma)

      json.tool can be used to validate json from the shell
      $echo '{"json":"obj"}' | python -mjson.tool
      {
          "json": "obj"
      }
      $echo '{1.2:3.4}' | python -mjson.tool
        Returns "Expecting property name enclosed in double quotes

      Tutorial here: http://pymotw.com/2/json/
"""

import json


def print_original_object(myobject):
    """ Helper function to find out what the original object is """
    print "Original object is type: ", type(myobject)
    print "Original object is: ", repr(myobject)


def print_returned_object(myobject):
    """ Helpter function to find out what the returned object is """
    print "Returned object is type: ", type(myobject)
    print "Returned object is: ", repr(myobject)


def encoding_basic_python_object():
    print "ENCODING BASIC PYTHON OBJECT"
    print "Example 1:"
    myobject = ['foo', {'bar': ('baz', None, 1.0, 2)}]
    print_original_object(myobject)
    #  Original object is type:  <type 'list'>
    #  Original object is  ['foo', {'bar': ('baz', None, 1.0, 2)}]
    a = json.dumps(myobject)
    print_returned_object(myobject)
    #  Returned object is type:  <type 'list'>
    #  Returned object is:  ['foo', {'bar': ('baz', None, 1.0, 2)}]

    print "Example 2:"
    myobject = {"c": 0, "b": 0, "a": 0}
    print_original_object(myobject)
    #  Original object is type:  <type 'dict'>
    #  Original object is  {'a': 0, 'c': 0, 'b': 0}
    b = json.dumps(myobject, sort_keys=True)
    print_returned_object(myobject)
    #  Returns type:  <type 'str'>
    #  Original object is:  {"a": 0, "b": 0, "c": 0}


def compact_encoding():
    print "COMPACT ENCODING"
    print "Example 1:"
    myobject = [1,2,3,{'4': 5, '6': 7}]
    print_original_object(myobject)
    #  Original object is type:  <type 'list'>
    #  Original object is  [1, 2, 3, {'4': 5, '6': 7}]
    c = json.dumps(myobject, separators=(',', ':'))
    print_returned_object(myobject)
    #  Returned object is type:  <type 'list'>
    #  Returned object is:  [1, 2, 3, {'4': 5, '6': 7}]


def pretty_print():
    print "PRETTY PRINTING (tldr; use indent to make it look nice"
    print "Example 1:"
    myobject = {'4': 5, '6': 7}
    print_original_object(myobject)
    #  Original object is type:  <type 'dict'>
    #  Original object is  {'4': 5, '6': 7}
    d = json.dumps(myobject, sort_keys=True,
                   indent=2, separators=(',', ':'))
    print type(d)  #<type 'str'>
    print d
    #{
    #  "4":5,
    #  "6":7,
    #}


def decoding_JSON():
    print "DECODING JSON"
    print "Example 1:"
    myobject = '["foo", {"bar":["baz", null, 1.0, 2]}]'
    print_original_object(myobject)
    #  Original object is type:  <type 'str'>
    #  Original object is  ["foo", {"bar":["baz", null, 1.0, 2]}]
    e = json.loads(myobject)
    print_returned_object(myobject)
    #  Returned object is type:  <type 'str'>
    #  Returned object is:  ["foo", {"bar":["baz", null, 1.0, 2]}]


#For specializing_JSON_object_decoding() example
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


def specializing_JSON_object_decoding():
    print "Specializing JSON object decoding"
    print "Example 1:"
    myobject = '{"__complex__": true, "real": 1, "imag": 2}'
    print_original_object(myobject)
    #  Original object is type:  <type 'str'>
    #  Original object is  {"__complex__": true, "real": 1, "imag": 2}
    f = json.loads(myobject,
                 object_hook=as_complex)  #(1+2j)
    print_returned_object(myobject)
    #  Returned object is type:  <type 'str'>
    #  Returned object is:  {"__complex__": true, "real": 1, "imag": 2}


def dumped_length():
    """ Shows different file sizes of each """
    print "DUMPED LENGTH"
    data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
    print 'DATA:', repr(data)  # DATA: [{'a': 'A', 'c': 3.0, 'b': (2, 4)}]
    print 'repr(data)             :', len(repr(data))  # 35
    print 'dumps(data)            :', len(json.dumps(data))  # 35
    print 'dumps(data, indent=2)  :', len(json.dumps(data, indent=2))  # 76
    print 'dumps(data, separators):', len(json.dumps(data, separators=(',',':')))  # 29


if __name__ == '__main__':
    encoding_basic_python_object()
    #compact_encoding()
    #pretty_print()
    #decoding_JSON()
    #specializing_JSON_object_decoding()
    #dumped_length()
