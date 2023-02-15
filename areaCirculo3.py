from manim import *

quality_factor = 1
fps = 30

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class areaCirculo3(Scene):
    def construct(self):
        ## Titulo y subtitulo
        title = MathTex(r'\text{¿Por qué el área del círculo es}',r'\,\pi r^2\,',r'\text{?}', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([ORANGE,GOLD, RED]).set_z_index(2)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT).set_z_index(2)

        subtitle = Tex('Método 3. Geometría').scale(0.6).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT).set_z_index(2)

        back_rect = BackgroundRectangle(VGroup(rect_title,brand,subtitle)).set_z_index(1)

        self.add(back_rect,title)
        self.play(Create(rect_title),FadeIn(brand), Write(subtitle))

        n_range = [5,30] #Intervalo cerrado
        poly_color = RED
        poly_a_color = ORANGE
        a_color = GREEN
        circle_color = RED

        circle = Circle(radius=2.2, color = circle_color).shift(LEFT*.7)
        circle_aux = circle.copy().set_stroke(width=1)

        polygon = RegularPolygon(n = n_range[0], radius=circle.radius/np.cos(PI/n_range[0]), color = poly_color).shift(circle.get_center()-ORIGIN)
        eq_n = MathTex(r'n=').next_to(subtitle,DOWN,aligned_edge=LEFT,buff= 1.5).shift(RIGHT*.2)
        n_num = Integer(n_range[0]).next_to(eq_n,RIGHT,aligned_edge=DOWN)

        self.play(Create(polygon), Write(eq_n), Write(n_num))
        self.play(Create(circle_aux))

        lines = VGroup()

        for point in polygon.get_points_defining_boundary():
            line = DashedLine(circle.get_center(),point,stroke_width = 1, color = poly_color)
            lines.add(line)

        self.play(Create(lines))

        a = Line(circle.get_bottom(),circle.get_center(),color = a_color)
        lbl_a = MathTex(r'apotema').rotate(PI/2).next_to(a,LEFT)

        self.play(Create(a),Write(lbl_a))

        self.wait()

        self.play(polygon.animate.set_fill(opacity = 0.5))

        eq_1 = MathTex(r'A',r'=',r'{\,\,P\,\,',r'\,a\,',r'\over',r'2').next_to(brand,DOWN,buff=0.5,aligned_edge = RIGHT).shift(LEFT*.2)
        eq_1[0].set_color(poly_a_color)
        eq_1[2].set_color(poly_color)
        eq_1[3].set_color(a_color)

        self.play(Write(eq_1), run_time = 0.7)
        self.play(Indicate(polygon),Indicate(eq_1[0]),color = poly_a_color,run_time = 2)
        self.play(polygon.animate.set_fill(opacity = 0))

        self.wait()

        self.play(FadeOut(lines), lbl_a.animate.become(MathTex(r'a').next_to(a,LEFT)))

        for i,n in enumerate(range(n_range[0]+1,n_range[1]+2)):

            rot = (PI/2+PI/n*(i+1)) if n%2==0 else PI/n*(i+1)

            if n == n_range[1]+1:
                polygon_aux = circle.rotate(rot+PI/2)
                n_num_aux = MathTex(r'\infty').move_to(n_num,aligned_edge = DOWN)
            else:
                n_num_aux = n_num.copy().set_value(n)
                polygon_aux = RegularPolygon(n = n, radius=circle.radius/np.cos(PI/n), color = poly_color).shift(circle.get_center()-ORIGIN).rotate(rot, about_point=circle.get_center())
            self.play(polygon.animate.become(polygon_aux), FadeOut(n_num,shift=UP*.5), FadeIn(n_num_aux,shift=UP*.5), run_time=np.exp(-1*i/10))
            self.remove(n_num)
            n_num = n_num_aux

        self.remove(circle_aux)

        self.play(lbl_a.animate.become(MathTex(r'r').next_to(a,LEFT)))
        lbl_p = MathTex(r'2',r'\pi',r'r').move_to(eq_1[2],aligned_edge = DOWN)
        lbl_r = MathTex(r'r').move_to(eq_1[3],aligned_edge = DOWN)

        self.play(FadeOut(eq_1[2],shift=UP*.5),FadeIn(lbl_p, target_position = circle.get_top()))
        self.play(Indicate(lbl_p,color=poly_color),Indicate(polygon,color=poly_color))
        self.play(FadeOut(eq_1[3],shift=UP*.5),FadeIn(lbl_r, target_position = lbl_a))
        self.play(Indicate(lbl_r,color=a_color),Indicate(a,color=a_color))

        self.wait(0.5)

        lbl_area = MathTex(r'\pi',r'r^',r'2').next_to(eq_1[0:2],aligned_edge = DOWN)

        self.play(FadeOut(lbl_p[0]),FadeOut(eq_1[4:]))
        self.play(
            TransformMatchingShapes(lbl_p[1],lbl_area[0]),
            TransformMatchingShapes(lbl_p[2],lbl_area[1]),
            TransformMatchingShapes(lbl_r[0],lbl_area[2]),
        )

        eq_f = VGroup(eq_1[0:2],lbl_area)

        self.play(polygon.animate.set_fill(color = poly_a_color, opacity = 0.6),eq_f.animate.scale(1.2).shift(DL*.5))
        self.play(Indicate(polygon, color = poly_a_color),Indicate(eq_f,color= poly_a_color))

        self.wait()
