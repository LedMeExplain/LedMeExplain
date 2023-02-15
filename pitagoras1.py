from manim import *

quality_factor = 1
fps = 30

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class pitagoras1(Scene):
    def construct(self):
        ## Titulo y subtitulo
        title = Tex(r'¿Cómo comprobar el Teorema de Pitágoras?', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([ORANGE, GREEN]).set_z_index(2)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT).set_z_index(2)

        subtitle = Tex('Método 1. Geometría').scale(0.6).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT).set_z_index(2)

        back_rect = BackgroundRectangle(VGroup(rect_title,brand,subtitle)).set_z_index(1)

        self.add(back_rect,title)
        self.play(Create(rect_title),FadeIn(brand), Write(subtitle))
        self.wait()

        pitagoras = VGroup()
        triangles = VGroup()
        labels = VGroup()

        vertices = [
            [ORIGIN,RIGHT*4,UP*3],
            [RIGHT,RIGHT+DOWN*4,RIGHT+RIGHT*3],
            [DR,DR+LEFT*4,DR+DOWN*3],
            [DOWN,DOWN+UP*4,DOWN+LEFT*3]
        ]

        a_dir = [RIGHT,DOWN,LEFT,UP]
        b_dir = [UP,RIGHT,DOWN,LEFT]
        c_dir = [UR,DR,DL,UL]

        for i in range(4):
            tr = Polygon(*vertices[i], fill_opacity = 0.7).set_color_by_gradient([BLUE,BLUE,TEAL])
            a = Tex('a', tex_template = TexFontTemplates.libertine).next_to((tr.get_vertices()[2]-tr.get_vertices()[0])/2+tr.get_vertices()[0],a_dir[i]).set_z_index(1)
            b = Tex('b', tex_template = TexFontTemplates.libertine).next_to((tr.get_vertices()[1]-tr.get_vertices()[0])/2+tr.get_vertices()[0],b_dir[i]).set_z_index(1)
            c = Tex('c', tex_template = TexFontTemplates.libertine).next_to((tr.get_vertices()[2]-tr.get_vertices()[1])/2+tr.get_vertices()[1],c_dir[i]).set_z_index(1)
            triangles.add(tr)
            labels.add(VGroup(a,b,c))

        square = Polygon(ORIGIN,RIGHT,DR,DOWN, fill_opacity = 0.7).set_color_by_gradient([BLUE,BLUE,TEAL])

        pitagoras.add(triangles,labels,square).scale(0.85).to_edge(LEFT)

        eq = MathTex(r'c^2',r'=',r'a^2',r'+',r'b^2', tex_template = TexFontTemplates.libertine).scale(1.5).next_to(subtitle,DOWN,buff=0.7,aligned_edge = LEFT).shift(RIGHT*1.5)

        for i in range(len(triangles)):
            if i == 0:
                self.play(DrawBorderThenFill(triangles[0]))
                self.wait()
                self.play(Write(labels[0]),lag_ratio = 0.5)
                self.wait(0.5)
            else :
                self.play(FadeIn(triangles[i]), run_time = 0.5)
                self.play(FadeIn(labels[i][2]), run_time = 0.2)
                self.wait(0.3)

        self.play(FadeIn(square))
        self.play(
            FadeOut(labels[0][0]),
            FadeOut(labels[0][1])
        )
        self.wait(0.5)

        self.play(FadeIn(eq[0]))

        square_c = VGroup(triangles,square)

        self.play(
            Indicate(square_c),
            Indicate(eq[0])
        )
        self.wait(0.5)

        self.play(
            Write(eq[1]),
            FadeOut(VGroup(*[i[2] for i in labels]))
        )

        self.wait(0.5)

        self.play(VGroup(triangles[3]).animate.shift(RIGHT*triangles[0].width+DOWN*triangles[2].height))
        labels[3].shift(RIGHT*triangles[0].width+DOWN*triangles[2].height)

        self.play(VGroup(triangles[0]).animate.shift(LEFT*triangles[3].width+DOWN*triangles[1].height))
        labels[0].shift(LEFT*triangles[3].width+DOWN*triangles[1].height)

        self.wait(0.5)
        self.play(
            Indicate(square_c),
            eq[0].animate.set_color(YELLOW)
        )

        self.wait(0.5)

        self.play(
            FadeIn(labels[0][0]),
            FadeIn(labels[3][1])
        )

        saORIGIN = triangles[0].get_vertices()[0]
        square_a = Polygon(saORIGIN,saORIGIN+RIGHT*square.width*3,saORIGIN+UR*square.width*3,saORIGIN+UP*square.width*3, fill_opacity = 0.7, color = GREEN)
        lbl_a = labels[0][0].copy().next_to(square_a.get_bottom(),UP).set_z_index(1)

        sbORIGIN = triangles[3].get_vertices()[0]
        square_b = Polygon(sbORIGIN,sbORIGIN+LEFT*square.width*4,sbORIGIN+UL*square.width*4,sbORIGIN+UP*square.width*4, fill_opacity = 0.7, color = RED)
        lbl_b = labels[3][1].copy().next_to(square_b.get_bottom(),UP).set_z_index(1)

        self.play(
            DrawBorderThenFill(square_a),
            FadeIn(eq[2]),
            FadeIn(lbl_a)
        )
        self.wait(0.5)

        self.play(
            Indicate(square_a, color=GREEN),
            eq[2].animate.set_color(GREEN)
        )

        self.play(Write(eq[3]))

        self.play(
            DrawBorderThenFill(square_b),
            FadeIn(eq[4]),
            FadeIn(lbl_b)
        )
        self.wait(0.5)

        self.play(
            Indicate(square_b, color=RED),
            eq[4].animate.set_color(RED)
        )

        self.wait()
