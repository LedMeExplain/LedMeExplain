from manim import *

quality_factor = 1

config['pixel_height'] = int(1080/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 8
config['frame_width'] = 8

class binomioCuadrado(Scene):
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


        a_len = 2
        b_len = 1
        color_0 = YELLOW
        color_a = RED
        color_b = BLUE
        color_ab = PURPLE
        fill_op = 0.7

        eq_1 = MathTex(r'(a+b)^2',r'=',r'a^2',r'+',r'2',r'ab',r'+',r'b^2', tex_template = TexFontTemplates.libertine).shift(UP*3)

        s_0 = Rectangle(height = a_len+b_len, width = a_len+b_len, color = WHITE)
        binomio_0 = VGroup(s_0)

        s_a = Rectangle(height= a_len, width=a_len, color = color_a, fill_opacity = fill_op)
        lbl_a = eq_1[2].copy().move_to(s_a)
        a = VGroup(s_a,lbl_a)

        s_b = Rectangle(height= b_len, width=b_len, color = color_b, fill_opacity = fill_op).next_to(s_a,UR,buff=0)
        lbl_b = eq_1[7].copy().move_to(s_b)
        b = VGroup(s_b,lbl_b)

        s_ab1 = Rectangle(height= b_len, width=a_len, color = color_ab, fill_opacity = fill_op).next_to(s_a,UP,buff=0)
        lbl_ab1 = eq_1[5].copy().move_to(s_ab1)
        ab1 = VGroup(s_ab1,lbl_ab1)

        s_ab2 = Rectangle(height= a_len, width=b_len, color = color_ab, fill_opacity = fill_op).next_to(s_a,RIGHT,buff=0)
        lbl_ab2 = eq_1[5].copy().move_to(s_ab2)
        ab2 = VGroup(s_ab2,lbl_ab2)

        binomio = VGroup(a,b,ab1,ab2)

        sc = 1.5

        binomio.scale(sc).move_to(ORIGIN)
        binomio_0.scale(sc).move_to(binomio)

        b_a1 = BraceLabel(s_a,'a',DOWN)
        b_b1 = BraceLabel(s_ab2,'b',DOWN)
        b_1 = VGroup(b_a1,b_b1)

        b_a2 = BraceLabel(s_a,'a',LEFT)
        b_b2 = BraceLabel(s_ab1,'b',LEFT)
        b_2 = VGroup(b_a2,b_b2)

        binomio_0.add(b_1,b_2)

        self.add(eq_1)
        self.add(binomio_0)
        self.add(binomio)

        self.wait(0.25)

        self.play(Indicate(eq_1[0],color=color_0),Indicate(s_0,color=color_0))

        self.play(Indicate(eq_1[2],color=color_a),Indicate(a,color=color_a))

        self.play(Indicate(eq_1[4:6],color=color_ab),Indicate(ab1,color=color_ab),Indicate(ab2,color=color_ab))

        self.play(Indicate(eq_1[7],color=color_b),Indicate(b,color=color_b))

        self.wait(0.25)
