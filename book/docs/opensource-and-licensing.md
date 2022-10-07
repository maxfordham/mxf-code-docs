# Opensource and Licensing

At Max Fordham the majority of our internal software-development projects utilise external opensource software. 
As a result, we believe that where possible, we should contribute back to the opensource community by 
making the code that we create publicly available. We also believe that openness and transparency
within Science and Engineering is good for society and encourages collaboration and innovation; this it put best by the 
non-profit [Numfocus](https://numfocus.org/): _"Open Code = Better Science"_.

In doing so we are placing ourselves in the same class as other industry leaders who are taking a similar approach, and
we are actively saying to other practioners that we are keen to share and learn, collaboratively.  

We also want to attract talent. Part of the joy of enjoying buildings is being part of something that contributes to
society as a whole: our designs end their life as public facing buildings, forming a dialogue between the engineer
and those who consume the buildings (either as users or just from the streetscape). We want this for our developers
too. They are not locked in the basement but are actively participating with other industry practicioners, and promoting
Max Fordham's engineering approach through the work they make public.

## Selecting a License

The decision to opensource a project is considered on a case by case basis; considering the benefit to the 
practice and the wider-industry. That said, precendents exist and can help guide future decisions.
Engineering Development at Max Fordham normally fits into two main categories, and broadly speaking 
the licensing follows the category:

### Developer Tools

- i.e. tools that we have made to make it easier for us to build tools
- `ipyautoui` and `ipyrun` fall into this category

**suggested licence**: _By default, use a **BSD license**. This is the most permissive licence and imposes no restrictions
on use by others. We feel this is appropriate as the code is not related to our income stream and we want others to use 
it and develop it without any restriction. The tools that we make often fit within an ecosystem of other BSD licensed
projects (e.g. Jupyter); by adopting the same license we are taking a collaborative and collegiate approach to the others
who operate in that ecosystem to build and share tools for others to use without restriction._

### Built-Environment Engineering Tools

- i.e. tools that help us deliver engineering work (our core business)
- `adaptive_comfort` and `aectemplater` are examples of this

**suggested licence**: _By default, use a **AGPLv3 license**. This requires others using the software to share changes they
might make to the source code, and declare theese changes publicly. In this case, the code is related to our core business. 
We want to encourage collaborators and competitors in the industry to use this code, but we want to restrict them from
building client-facing products and services from it without declaring associated developments back to the core codebase._
 
## When would we choose not to share? 

If we made a tool that we wanted to develop into a unique offering to clients, where the exclusivity of use would present
an opportunity to Max Fordham, we might decide not to share the tool publicly.
 
```{note}
Both licences suggested above have clauses that remove liability from the author
and make clear that the code is provided "as is".
```

```{note}
Always consider the packages that you rely on when thinking about the license... 
e.g. giving a (more-permissive) BSD license to a package that relies wholly on a 
GNU package could be misleading to the end-user. Equally packaging something as
GNU when the ecosystem within which it exist is BSD could place unnecessary
restrictions on those using the tool, and doesn't engage with the collective
decisions of the community it belongs.
```
