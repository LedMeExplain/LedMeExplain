from manim import *

quality_factor = 1
fps = 30

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class senCos(Scene):
    def construct(self):
        ## Titulo y subtitulo
        title = Tex(r'¿Cómo se ven el $\sen(x)$ y el $\cos(x)$?', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([LME_A, WHITE,LME_A]).set_z_index(2)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT).set_z_index(2)

        subtitle = Tex('Trigonometría').scale(0.6).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT).set_z_index(2)

        back_rect = BackgroundRectangle(VGroup(rect_title,brand,subtitle)).set_z_index(1)

        self.add(back_rect,title)
        self.play(Create(rect_title),FadeIn(brand), Write(subtitle))

        self.rate = 0.25
        self.pi = 1
        self.rad = 1
        self.origin_point = LEFT*2 + UP*2.5
        self.curve_start = self.origin_point + RIGHT*self.rad
        self.curve_start_cos = self.origin_point + DR*self.rad
        self.x_len = 6
        self.y_len = 6

        circle = Circle(radius=2, color = GREEN).shift(LEFT)
        r = Line(circle.get_center(),circle.get_center()+RIGHT*circle.radius, color = GREEN, stroke_width = 2)
        lbl_r = MathTex(r'r = 1').scale(0.8).next_to(r,UP)
        self.play(Create(circle))
        self.play(Create(r),Write(lbl_r))
        self.wait(0.5)
        self.play(Unwrite(lbl_r))

        hip = Line(circle.get_center(),circle.point_from_proportion(0.1), color = YELLOW)
        lbl_hip = Tex(r'Hipotenusa').set_color(YELLOW).scale(0.7).rotate(TAU*.1).move_to(hip).shift(UL*.25)

        co = DashedLine(hip.get_end(),np.array([hip.get_end()[0],circle.get_center()[1],0]), color = TEAL)
        lbl_co = Tex(r'Cateto \\ Opuesto').set_color(TEAL).scale(0.7).next_to(co,RIGHT,buff=0.5)

        ca = DashedLine(hip.get_start(),np.array([hip.get_end()[0],circle.get_center()[1],0]), color = ORANGE)
        lbl_ca = Tex(r'Cateto \\ Adyacente').set_color(ORANGE).scale(0.7).next_to(ca,DOWN)

        a = Angle(ca, hip, radius=0.5, other_angle=False)
        lbl_a = MathTex(r"x").scale(0.6). move_to(
            Angle(
                ca, hip, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        self.play(Create(hip),Write(lbl_hip))

        self.play(Create(a),Write(lbl_a))

        self.play(Create(co),Write(lbl_co))

        self.play(Create(ca),Write(lbl_ca))

        eq_1 = MathTex(r"\sen(x)",r"=",r"{CO",r"\over",r"HIP}").scale(0.8)
        eq_1[2].set_color(TEAL)
        eq_1[4].set_color(YELLOW)

        eq_2 = MathTex(r"\cos(x)",r"=",r"{CA",r"\over",r"HIP}").scale(0.8)
        eq_2[2].set_color(ORANGE)
        eq_2[4].set_color(YELLOW)

        eq_group = VGroup(eq_1,eq_2).arrange(buff= 1).next_to(rect_title,DOWN,buff=1)

        self.play(Write(eq_1),run_time = 0.7)
        self.play(Write(eq_2),run_time = 0.7)

        self.wait()
        self.play(
            FadeOut(VGroup(hip,lbl_hip,co,lbl_co,ca,lbl_ca,a,lbl_a,r)),
            eq_1.animate.next_to(brand,DOWN,aligned_edge = RIGHT),
            eq_2.animate.move_to(RIGHT*.5+DOWN*2.5),
            circle.animate.scale(0.5).move_to(self.origin_point)
        )
        self.circle = circle

        self.show_axis()
        self.move_dot_and_draw_curve()

        self.wait(0.5)

        self.play(
            FadeOut(self.circle),
            FadeOut(self.dot),
            FadeOut(self.origin_to_circle_line),
            FadeOut(self.dot_to_curve_line),
            FadeOut(self.dot_to_curve_line_cos),
            self.y_axis[0].animate.become(Line(self.origin_point+self.rad*DOWN,self.origin_point+(self.y_len-0.5)*DOWN, stroke_width = 1)),
            self.x_axis[0].animate.become(Line(self.origin_point+self.rad*RIGHT,self.origin_point+(self.x_len-0.5)*RIGHT, stroke_width = 1)),
            *[lbl.animate.rotate(-PI/2) for lbl in self.y_axis_lbl]
        )

        self.wait(0.5)

        cos = VGroup(self.y_axis,self.cos_curve_line)
        sin = VGroup(self.x_axis,self.sine_curve_line)

        self.play(
            cos.animate.rotate(PI/2).next_to(sin,DOWN,buff=2,aligned_edge = RIGHT),
            eq_2.animate.next_to(brand,DOWN,buff=3.5,aligned_edge=RIGHT)
        )

        self.play(
            sin.animate.shift(LEFT*2.5+DOWN*.5),
            cos.animate.shift(LEFT*2.5),
            eq_2.animate.next_to(brand,DOWN,buff=4,aligned_edge=RIGHT).shift(LEFT*.5),
            eq_1.animate.next_to(brand,DOWN,buff=1,aligned_edge=RIGHT).shift(LEFT*.5),
        )

        self.wait()

    def show_axis(self):
        self.x_axis = VGroup()
        self.y_axis = VGroup()

        x_line = Line(self.origin_point+(self.rad+0.5)*LEFT,self.origin_point+(self.x_len-0.5)*RIGHT, stroke_width = 1)
        y_line = Line(self.origin_point+(self.rad+0.5)*UP,self.origin_point+(self.y_len-0.5)*DOWN, stroke_width = 1)

        self.x_axis.add(x_line)
        self.y_axis.add(y_line)

        self.play(Create(x_line),Create(y_line))
        self.add_x_labels()
        self.add_y_labels()

    def add_x_labels(self):
        s = 0.7
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            tip = Line(ORIGIN,UP*.1,stroke_width=2).move_to(np.array([self.curve_start[0] + (i+1)/self.pi, self.origin_point[1], 0]))
            x_labels[i].scale(s).next_to(np.array([self.curve_start[0] + (i+1)/self.pi, self.origin_point[1], 0]), DOWN)
            self.x_axis.add(tip,x_labels[i])
            self.play(Write(x_labels[i]),Write(tip),run_time = 0.2)

    def add_y_labels(self):
        s = 0.7
        y_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]
        self.y_axis_lbl = VGroup()
        for i in range(len(y_labels)):
            tip = Line(ORIGIN,RIGHT*.1,stroke_width=2).move_to(np.array([self.origin_point[0],self.curve_start_cos[1] - (i+1)/self.pi, 0]))
            y_labels[i].scale(s).next_to(np.array([self.origin_point[0],self.curve_start_cos[1] - (i+1)/self.pi, 0]), LEFT)
            self.y_axis.add(tip,y_labels[i])
            self.y_axis_lbl.add(y_labels[i])
            self.play(Write(y_labels[i]),Write(tip),run_time = 0.2)

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        self.dot = Dot(radius=0.05, color=WHITE).set_z_index(1)
        self.dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0

        def go_around_circle(mob, dt):
            self.t_offset += (dt * self.rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, self.dot.get_center(), color=YELLOW)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset*2*self.pi
            y = self.dot.get_center()[1]
            return Line(self.dot.get_center(), np.array([x,y,0]), color=TEAL, stroke_width=2 )

        def get_line_to_curve_cos():
            x = self.dot.get_center()[0]
            y = self.curve_start_cos[1] - self.t_offset*2*self.pi
            return Line(self.dot.get_center(), np.array([x,y,0]), color=ORANGE, stroke_width=2 )

        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset*2*self.pi
            y = self.dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=TEAL)
            self.curve.add(new_line)

            return self.curve

        self.curve_cos = VGroup()
        self.curve_cos.add(Line(self.curve_start_cos,self.curve_start_cos))
        def get_curve_cos():
            last_line = self.curve_cos[-1]
            x = self.dot.get_center()[0]
            y = self.curve_start_cos[1] - self.t_offset*2*self.pi
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=ORANGE)
            self.curve_cos.add(new_line)

            return self.curve_cos

        self.dot.add_updater(go_around_circle)

        self.origin_to_circle_line = always_redraw(get_line_to_circle)
        self.dot_to_curve_line = always_redraw(get_line_to_curve)
        self.dot_to_curve_line_cos = always_redraw(get_line_to_curve_cos)
        self.sine_curve_line = always_redraw(get_curve)
        self.cos_curve_line = always_redraw(get_curve_cos)

        self.add(self.dot)
        self.add(orbit, self.origin_to_circle_line, self.dot_to_curve_line, self.dot_to_curve_line_cos, self.sine_curve_line, self.cos_curve_line)
        self.wait(8.5)

        self.dot.remove_updater(go_around_circle)
