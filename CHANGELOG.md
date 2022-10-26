# Release notes

<!-- do not remove -->

## 0.0.5




## 0.0.4

### New Features

- Inspector: display scrollbar when exceeding maximum height or width ([#11](https://github.com/tylere/earthengine-jupyter/issues/11))

- Inspector: Simplify the object display by using OrderedDict ([#10](https://github.com/tylere/earthengine-jupyter/issues/10))
  - The object folder's display logic currently hardcodes the keys that it expects to display. It could be better to order the keys that are returned by ee.Object.getInfo().

- Map: Display crosshairs when cursor is over the map ([#9](https://github.com/tylere/earthengine-jupyter/issues/9))

- Provide map view details in the Inspector's Point folder ([#5](https://github.com/tylere/earthengine-jupyter/issues/5))

- Inspector: return "No unmasked pixels at clicked point." for layers with fully masked bands ([#2](https://github.com/tylere/earthengine-jupyter/issues/2))

- Inspector: disable Pixels & Objects folders if there are non map layers ([#1](https://github.com/tylere/earthengine-jupyter/issues/1))
  - Similar to the Code Editor, only display the Pixels and Objects folders if the map has layers


## 0.0.3


### Bugs Squashed

- Having code in package to install itself doesn't work ([#12](https://github.com/google/earthengine-jupyter/issues/12))


## 0.0.2

### New Features

- Add colab setup function ([#11](https://github.com/google/earthengine-jupyter/issues/11))
  - Add a function to simplify setting up Colab (install packages, authenticate).



## 0.0.1

### New Features

- Rename library to be more consistent with Earth Engine client library ([#3](https://github.com/google/earthengine-jupyter/issues/3))
  - earthengine_jupyter -> ee_jupyter

- Create initial content ([#2](https://github.com/google/earthengine-jupyter/issues/2))
  - An initial issue intended to exercising the changelog, release, and push to PyPI.



