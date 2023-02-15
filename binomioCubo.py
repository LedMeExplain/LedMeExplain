from manim import *

quality_factor = 1

config['pixel_height'] = int(1080/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 8
config['frame_width'] = 8

config["tex_template"] = TexFontTemplates.libertine

class binomioCuboFB(Scene):
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
        color_0 = LIGHT_PINK
        color_a = RED
        color_b = BLUE
        color_a2b = GREEN
        color_ab2 = GOLD
        fill_op = 0.7

        eq_1 = MathTex(r'(a+b)^3',r'=',r'a^3',r'+',r'3',r'a^2b',r'+',r'3',r'ab^2',r'+',r'b^3', tex_template = TexFontTemplates.libertine).to_edge(UP)

        s_0 = Cube(side_length=a_len+b_len, fill_color = color_0, stroke_width = 3).set_fill(opacity=0)

        a1 = BraceBetweenPoints(s_0.get_corner(DL+OUT),s_0.get_corner(DR+OUT)+LEFT)
        a1.add(a1.get_tex(r'a').scale(0.8))
        b1 = BraceBetweenPoints(s_0.get_corner(DR+OUT)+LEFT,s_0.get_corner(DR+OUT))
        b1.add(b1.get_tex(r'b').scale(0.8))

        a3 = BraceBetweenPoints(s_0.get_corner(DR+IN),s_0.get_corner(UR+IN)+DOWN)
        a3.add(a3.get_tex(r'a').scale(0.8))
        b3 = BraceBetweenPoints(s_0.get_corner(UR+IN)+DOWN,s_0.get_corner(UR+IN))
        b3.add(b3.get_tex(r'b').scale(0.8))

        lbl_0 = eq_1[0].copy().move_to(s_0.get_zenith()).set_z_index_by_z_coordinate()

        s_b = Prism(dimensions = [b_len,b_len,b_len], fill_color = color_b, stroke_width = 3).shift(OUT+UR)
        s_a = Prism(dimensions = [a_len,a_len,a_len], fill_color = color_a, stroke_width = 3).next_to(s_b,DL+IN,buff=0)
        s_a2b_1 = Prism(dimensions = [a_len,a_len,b_len], fill_color = color_a2b, stroke_width = 3).next_to(s_b,DL,buff=0)
        s_a2b_2 = Prism(dimensions = [b_len,a_len,a_len], fill_color = color_a2b, stroke_width = 3).next_to(s_b,DOWN+IN,buff=0)
        s_a2b_3 = Prism(dimensions = [a_len,b_len,a_len], fill_color = color_a2b, stroke_width = 3).next_to(s_b,LEFT+IN,buff=0)
        s_ab2_1 = Prism(dimensions = [a_len,b_len,b_len], fill_color = color_ab2, stroke_width = 3).next_to(s_b,LEFT,buff=0)
        s_ab2_2 = Prism(dimensions = [b_len,a_len,b_len], fill_color = color_ab2, stroke_width = 3).next_to(s_b,DOWN,buff=0)
        s_ab2_3 = Prism(dimensions = [b_len,b_len,a_len], fill_color = color_ab2, stroke_width = 3).next_to(s_b,IN,buff=0)

        lbl_a = eq_1[2].copy().move_to(s_a.get_zenith()).set_z_index_by_z_coordinate()
        lbl_a2b_1 = eq_1[5].copy().move_to(s_a2b_1.get_zenith()).set_z_index_by_z_coordinate()
        lbl_ab2_1 = eq_1[8].copy().move_to(s_ab2_1.get_zenith()).set_z_index_by_z_coordinate()
        lbl_b = eq_1[10].copy().move_to(s_b.get_zenith()).set_z_index_by_z_coordinate()

        for mob in [s_0,s_a,s_a2b_1,s_a2b_2,s_a2b_3,s_ab2_1,s_ab2_2,s_ab2_3,s_b]:
            for sub in mob:
                sub.set_z_index_by_z_coordinate()
            mob[3].set_z_index(mob[5].z_index)
            mob[5].z_index-=0.01

        rot = PI/9
        binomio_0 = VGroup(s_0,s_a,s_a2b_1,s_a2b_2,s_a2b_3,s_ab2_1,s_ab2_2,s_ab2_3,s_b,a1,b1,a3,b3,lbl_0,lbl_a,lbl_a2b_1,lbl_ab2_1,lbl_b).rotate(rot,axis = -Y_AXIS+X_AXIS)


        a2 = BraceBetweenPoints(s_0.get_corner(DR)+LEFT*2/3*np.cos(rot)+UP*1/3*np.sin(PI/2-rot),s_0.get_corner(DR)+UP*np.sin(PI/2-rot),buff=0.3)
        a2.add(a2.get_tex(r'a').scale(0.8))
        b2 = BraceBetweenPoints(s_0.get_corner(DR)+LEFT*np.cos(rot),s_0.get_corner(DR)+LEFT*2/3*np.cos(rot)+UP*1/3*np.sin(PI/2-rot),buff=0.3)
        b2.add(b2.get_tex(r'b').scale(0.8))

        binomio_0.add(a2,b2).scale(1.2)

        self.add(eq_1[0])
        self.add(s_0)
        self.add(a1,b1,a2,b2,a3,b3)

        self.play(s_0.animate.set_fill(opacity=0.7))
        self.play(FadeIn(lbl_0))
        self.play(Indicate(eq_1[0],color=color_0),Indicate(s_0,color=color_0))

        self.play(s_0.animate.set_fill(opacity=0),FadeOut(lbl_0))

        self.play(Write(eq_1[1]),run_time = 0.7)

        self.play(Write(eq_1[2]),run_time = 0.7)
        self.play(FadeIn(s_a),FadeIn(lbl_a))
        self.play(Indicate(eq_1[2],color=color_a),Indicate(s_a,color=color_a))

        self.play(Write(eq_1[3]),FadeOut(lbl_a),run_time = 0.7)

        self.play(Write(eq_1[4:6]),run_time = 0.7)
        self.play(FadeIn(s_a2b_1),FadeIn(lbl_a2b_1),run_time = 2/3)
        self.play(FadeIn(s_a2b_2),run_time = 2/3)
        self.play(FadeIn(s_a2b_3),run_time = 2/3)
        self.play(Indicate(eq_1[4:6],color=color_a2b),Indicate(s_a2b_1,color=color_a2b),Indicate(s_a2b_2,color=color_a2b),Indicate(s_a2b_3,color=color_a2b))

        self.play(Write(eq_1[6]),FadeOut(lbl_a2b_1),run_time = 0.7)

        self.play(Write(eq_1[7:9]),run_time = 0.7)
        self.play(FadeIn(s_ab2_1),FadeIn(lbl_ab2_1),run_time = 2/3)
        self.play(FadeIn(s_ab2_2),run_time = 2/3)
        self.play(FadeIn(s_ab2_3),run_time = 2/3)
        self.play(Indicate(eq_1[7:9],color=color_ab2),Indicate(s_ab2_1,color=color_ab2),Indicate(s_ab2_2,color=color_ab2),Indicate(s_ab2_3,color=color_ab2))

        self.play(Write(eq_1[9]),FadeOut(lbl_ab2_1),run_time = 0.7)

        self.play(Write(eq_1[10]),run_time = 0.7)
        self.play(FadeIn(s_b),FadeIn(lbl_b))
        self.play(Indicate(eq_1[10],color=color_b),Indicate(s_b,color=color_b))

        self.play(FadeOut(lbl_b),run_time = 0.7)

        self.wait()

        self.play(FadeOut(eq_1[1:]),FadeOut(s_a,s_a2b_1,s_a2b_2,s_a2b_3,s_ab2_1,s_ab2_2,s_ab2_3,s_b))
