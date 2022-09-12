# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_map.ipynb.

# %% auto 0
__all__ = ['DEFAULT_MAP_HEIGHT', 'TileLayerEE', 'JupyterMap']

# %% ../00_map.ipynb 4
import ee
import ipyleaflet
import ipywidgets as widgets
import traitlets

DEFAULT_MAP_HEIGHT = '400px'

class TileLayerEE(ipyleaflet.TileLayer):
  """Class for a tile layer generated by Earth Engine.
  
  Attributes:
    ee_object: An Earth Engine object.
  """
  def __init__(self, ee_object, *args, **kwargs):

    self.ee_object = ee_object

    super(TileLayerEE, self).__init__(*args, **kwargs)


class JupyterMap(ipyleaflet.Map):
  """An interactive map class for Jupyter clients.
  
  Attributes:
    layers_control: a boolean indicating whether to display a layers control.
  """

  layers_control = traitlets.Bool(True)

  def __init__(self, *args, **kwargs):

    self.layers_control_instance = None

    # Set default values for the map.
    if 'zoom' not in kwargs:
      kwargs['zoom'] = 4
    
    if 'basemap' not in kwargs:
      kwargs['basemap'] = ipyleaflet.basemap_to_tiles(ipyleaflet.basemaps.Stamen.Watercolor)

    if 'height' not in kwargs:
      kwargs['height'] = DEFAULT_MAP_HEIGHT
    
    super(JupyterMap, self).__init__(*args, **kwargs)
    
    if self.layers_control:
      self.layers_control_instance = ipyleaflet.LayersControl(position='topright')
      self.add_control(self.layers_control_instance)
        
    self.default_style.cursor = 'crosshair'
        
  def addLayer(self, eeObject, visParams={}, name=None, shown=True, opacity=1):
    """Adds a layer for an Earth Engine object."""
    
    if name is None:
      # Provide a default name for the layer in the form "Layer ##"
      name = f'Layer {len(self.layers)}'

    def get_tile_layer_url(ee_image_object):
      map_id_dict = ee.Image(ee_image_object).getMapId()
      return map_id_dict['tile_fetcher'].url_format

    # Assume that the eeObject is an ee.Image.
    # TODO: Generalize this to other EE objects.
    ee_image = eeObject

    tile_url = get_tile_layer_url(
      ee_image.visualize(**visParams)
    )
    self.add_layer(TileLayerEE(ee_object=eeObject, url=tile_url, name=name, visible=shown))
