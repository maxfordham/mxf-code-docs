# Developing

## Intro

there are 2no main strands of internal software development:

- Standalone Development
  - Software that is developed independently of a piece of software. This software can interface
    the core MF software (by passing data between the apps) but does not have direct access to the software API's.
  - Typically runs on the jupyter server.
    - Ad-hoc jupyter notebooks for a given job.
    - Standalone Apps built using Voila and ipywidgets.

- Software Automation
  - pyRevit
    - pyRevit is used to automate Revit processes. It is described as RAD (Rapid Application Development),
      making it fast to build utility scripts the Revit application.
  - IES VEscripts
  - Rhino + Grasshopper + Python (currently Light and Air only)


## Standalone Development

### User interfaces and visual experiences

The jupyter ecosystem has a rich selection of packages that can be used to make high-quality front-ends.

| package      | description                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------------------- |
| voila        | converts a jupyter notebook (.ipynb) into a standalone app                                                            |
| ipywidgets   | core widget library with common UI components                                                                         |
| ipydatagrid  | fast, performant datagrid, featuring: filters, cell editing, cell rendering, etc.                                     |
| bqplot       | 2D plotting library based on the "The Gramma of Graphics". Facilitates customisable complex interactions.             |
| altair       | 2D plotting library based on the "The Gramma of Graphics". Python binding of vegalite. Excellent for simple plotting. |
| plotly       | Plotting library. Generally prefer the above, but plotly also very good! Supports 3D plotting.                        |
| ipycytoscape | widget enabling interactive graph visualization                                                                       |
| ipygany      | 3D visualisation widget                                                                                               |
| pydeck       | 3D visualisation widget built using deck.gl                                                                           |
|              |                                                                                                                       |

## Software Automation

add brief description here.