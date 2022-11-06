def balance(st):
    '''
       Function to check if sequence contains valid parenthesis
       :param sequence: Sequence of brackets
       :return: True is sequence is valid else False
       '''
       # Replace the proper pairs until sequence becomes empty or no pairs are present
    while True:
        if '()' in st:
            st = st.replace('()', '')
        elif '{}' in st:
            st = st.replace('{}', '')
        elif '[]' in st:
            st = st.replace('[]', '')
        else:
            return not st

bal = balance("{()[]{}}")
if bal:
    print("balanced string")
else:
    print("Not balanced string")
