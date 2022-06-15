# Opensource and Licensing

At Max Fordham the majority of our internal development utilises external opensource software. 
As a result, we believe that where possible, we should contribute back to the opensource community by 
making the code that we create and use publicly available. We also believe that openness and transparency
within Science and Engineering is good for society and encourages innovation; this it put best by the 
non-profit [Numfocus](https://numfocus.org/): _"Open Code = Better Science"_.

Engineering Development at Max Fordham normally fits into two main categories, and broadly speaking 
the licensing follows the category:

## developer tools

- i.e. tools that we have made to make it easier for us to build tools
- `ipyautoui` and `ipyrun` fall into this category

### licence

By default, use a __BSD license__. This is because this code is not related to our income stream and we want 
others to use it without any restriction. 

## engineering tools

- i.e. tools that help us deliver engineering work (our core business)
- `adaptive_comfort` and `aectemplater` are examples of this
  
### licence

By default, use a __AGPLv3 license__. This is because this code is related to our core business. We want to 
encourage collaborators and competitors in the industry to use this code, but we want to restrict them from 
building client-facing products and services from it without contributing back to the core codebase.
 
```{note}
Always consider the packages that you rely on when thinking about the license... 
e.g. giving a (more-permissive) BSD license to a package that relies wholly on a 
GNU package could be misleading to the end-user. 
```

```{note}
The above can be taken as a general principle but everytime a package is opensourced this 
should be considered on a case by case basis. 
```