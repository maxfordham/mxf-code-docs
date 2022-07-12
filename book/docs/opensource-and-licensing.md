# Opensource and Licensing

At Max Fordham the majority of our internal software-development projects utilise external opensource software. 
As a result, we believe that where possible, we should contribute back to the opensource community by 
making the code that we create publicly available. We also believe that openness and transparency
within Science and Engineering is good for society and encourages collaboration and innovation; this it put best by the 
non-profit [Numfocus](https://numfocus.org/): _"Open Code = Better Science"_.

In doing so we are placing ourselves in the same class as other industry leaders who are taking a similar approach, and
we are actively saying to other practioners that we are keen to share and learn, collaboratively.  

The decision to opensource a project is considered on a case by case basis; considering the benefit to the 
practice and the wider-industry. That said, precendents exist and can help guide future decisions.
Engineering Development at Max Fordham normally fits into two main categories, and broadly speaking 
the licensing follows the category:

## developer tools

- i.e. tools that we have made to make it easier for us to build tools
- `ipyautoui` and `ipyrun` fall into this category

**suggested licence**: _By default, use a **BSD license**. This is the most permissive licence and imposes no restrictions
on use by others. We feel this is appropriate as the code is not related to our income stream and we want others to use 
it and develop it without any restriction. The tools that we make often fit within an ecosystem of other BSD licensed
projects (e.g. Jupyter); by adopting the same license we are taking a collaborative and collegiate approach to the others
who operate in that ecosystem to build and share tools for others to use without restriction._

## engineering tools

- i.e. tools that help us deliver engineering work (our core business)
- `adaptive_comfort` and `aectemplater` are examples of this

**suggested licence**: _By default, use a **AGPLv3 license**. This requires others using the software to share changes they
might make to the source code, and declare theese changes publicly. In this case, the code is related to our core business. 
We want to encourage collaborators and competitors in the industry to use this code, but we want to restrict them from
building client-facing products and services from it without declaring associated developments back to the core codebase._
 
what don't we share?
 
```{note}
Both licences suggested above have clauses that remove liability from the author
and make clear that the code is provided "as is".
```

```{note}
Always consider the packages that you rely on when thinking about the license... 
e.g. giving a (more-permissive) BSD license to a package that relies wholly on a 
GNU package could be misleading to the end-user. 
```
