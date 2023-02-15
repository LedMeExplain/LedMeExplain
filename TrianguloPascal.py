from manim import *
import numpy as np

quality_factor = 1

config['pixel_height'] = int(1080/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 8
config['frame_width'] = 8

config["tex_template"] = TexFontTemplates.libertine

class trianguloPascalFB(Scene):
    def construct(self):

        ##------------------------------
        ## Logo LME en la esquina
        ##------------------------------
        brand = Text(
            "LED Me Explain",
            fill_opacity = 0.5,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).to_edge(DR*.8).set_z_index(2)
        # Añade el logo
        self.add(brand)
        ##---------------------------------
        ##---------------------------------

        def Pascal(rows = 5, colors = ['#236B8E', '#83C167', '#FFFF00', '#FC6255'], height = None, width = None):
            pas_tri = VGroup()
            color_array = color_gradient(colors,rows)
            for n in range(rows):
                for k in range(n+1):
                    hex = RegularPolygon(n=6, color = color_array[n], fill_opacity=0.7, stroke_width = DEFAULT_STROKE_WIDTH*6/(rows+1)).rotate(PI/2).shift(DOWN*n*(1+np.sin(PI/6))+RIGHT*(n-k*2)*np.cos(PI/6))
                    num = int(np.math.factorial(n)/np.math.factorial(k)/np.math.factorial(n-k))
                    lbl = Text(str(num)).rescale_to_fit(max(hex.width,hex.height)*0.4,[0,1]).move_to(hex)
                    pas_tri.add(VGroup(hex,lbl))

            if width is not None:
                pas_tri.scale_to_fit_width(width)
            elif height is not None:
                pas_tri.scale_to_fit_height(height)
            else:
                pas_tri.scale_to_fit_width(config['frame_width']*0.9)

            pas_tri.move_to(ORIGIN)
            return pas_tri

        pascal = Pascal(11)

        self.add(pascal)
