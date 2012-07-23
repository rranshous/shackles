def normalize_chain(chain):
    """
    Convenience method formatting attribute chain into iterables.
    """
    if isinstance(chain, (str, unicode)):
        chain = chain.split('.')

    if not isinstance(chain, (list, tuple)):
        raise Exception
    return chain

def broken(obj, chain):
    """Return name of attribute where the chain
    is broken.

    If chain is not broken (all attributes are represented in chain)
    nothing is returned."""
    chain = normalize_chain(chain)

    for attr in chain:
        obj = getattr(obj, attr, None)
        if not obj:
            return attr

def get(obj, chain, *args):
    """Recursively walk chain. Return the value
    of the final named attribute in the chain.

    If a named attribute does not exist,
    default is returned if provided, otherwise AttributeError is raised.

    Replaces doing things like:
    object.attr1.attr2.attr3 if object and object.attr1.attr2 else None

    or

    getattr(getattr(getattr(object, 'attr1', None), 'attr2', None), 'attr3', None)
    """
    dflt_set = False

    if args:
        if len(args) != 1:
            raise TypeError, '{0} expected at most 3 arguments, got {1}'.format(
                'get', len(args))
        dflt = args[0]
        dflt_set = True

    chain = normalize_chain(chain)

    for attr in chain:
        obj = getattr(obj, attr, dflt) if dflt_set else getattr(obj, attr)
        if not obj:
            raise AttributeError
    return obj

def walk(obj, chain):
    pass
