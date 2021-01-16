def deep_keys(dct):
   if not isinstance(dct, (dict, list)):
      return ['']
   if isinstance(dct, list):
      return [dk for x in dct for dk in deep_keys(x)]
   return [(dk if dk else k) for k, v in dct.items() for dk in deep_keys(v)]
   