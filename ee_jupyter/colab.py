# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_colab.ipynb.

# %% auto 0
__all__ = ['set_colab_output_cell_height']

# %% ../nbs/00_colab.ipynb 3
def set_colab_output_cell_height(max_height):
    """Sets the maximum height for the current notebook cell's output."""
    import google
    
    from IPython.display import Javascript
    from string import Template
    s = Template('google.colab.output.setIframeHeight(0, true, {maxHeight: $height})')
    display(Javascript(s.substitute(height=max_height)))