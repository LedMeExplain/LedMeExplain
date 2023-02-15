from manim import *

##------------------------------
## Tiktok config
##------------------------------
#config.pixel_height = 1920
#config.pixel_width = 1080
#config.frame_height = 14
#config.frame_width = 8
##---------------------------------
##---------------------------------

LME_color = "#27a0b3"

class ExpZ_1(Scene):
    def construct(self):

        ##------------------------------
        ## Logo LME en la esquina
        ##------------------------------
        brand = Text(
            "LED Me Explain",
            fill_opacity = 0.5,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_color,"[3:4]":LME_color,"[5:6]":LME_color} ## Los espacios no cuentan como caracteres
        ).scale(0.4).to_edge(DR)
        # Añade el logo
        self.add(brand)
        ##---------------------------------
        ##---------------------------------

        ##------------------------------
        ## Titulo y subtitulo del video
        ##------------------------------
        title = Tex( # Crea el título
            r"¿Cómo se ve la transformación ", r'$z$',r'$\,\rightarrow\,$',r'$e^z$',r' ?',
        ).scale_to_fit_width(config["frame_width"]-4)
        title_math = MathTex(r'z',r'\rightarrow',r'e^z', tex_template = TexFontTemplates.libertine).move_to(title[2], aligned_edge = DOWN).scale(1.2).shift(RIGHT*.1)
        title_math[0].set_color(TEAL_C)
        title_math[2].set_color(PURPLE_C)

        # Crea el rectangulo que rodea al grupo
        frameTitle = SurroundingRectangle(title, LME_color, buff = 1)

        subtitle = Text( # Crea el subtítulo
            "Variable Compleja",
            color = LIGHT_GREY
        ).scale(0.6).next_to(frameTitle,DOWN, aligned_edge = RIGHT)


        # Aparece el titulo
        self.play(
            FadeIn(title[0]),
            FadeIn(title[4]),
            FadeIn(title_math)
        )
        # Crea el rectangulo
        self.play(Create(frameTitle))
        # Escribe el subtitulo
        self.play(Write(subtitle) , run_time = 0.7)
        self.wait(1.5) # Espera un momento
        # Desaparece el titulo, subtitulo y el rectangulo
        self.play(
            FadeOut(title[0], scale=0.7),
            FadeOut(title[4], scale=0.7),
            FadeOut(title_math, scale = 0.7),
            FadeOut(subtitle, scale=0.7),
            FadeOut(frameTitle)
        )
        ##---------------------------------
        ##---------------------------------

        ##------------------------------
        ## 1. Título, enunciado y animación del problema
        ##------------------------------
        header = Title(r'Esta es la transformación ',r'$z$',r'$\,\rightarrow\,$',r'$e^z$', scale_factor = 1.5).set_z_index(1)
        header_math = MathTex(r'z',r'\rightarrow',r'e^z', tex_template = TexFontTemplates.libertine).move_to(header[2], aligned_edge = DOWN).scale(1.4).shift(UR*0.1).set_z_index(1)
        header_math[0].set_color(TEAL_C)
        header_math[2].set_color(PURPLE_C)

        self.play(
            FadeIn(header[0]),
            FadeIn(header[-1]),
            FadeIn(header_math)
        )
        self.wait()

        square_1 = Square(color = TEAL_C)
        rectPlane = NumberPlane(x_range=(-8, 8, 1)).set_opacity(0.3)

        lbl_x_axis = MathTex(r'Re', tex_template = TexFontTemplates.libertine).next_to(RIGHT*5,UP).set_opacity(0.3)
        lbl_y_axis = MathTex(r'Im', tex_template = TexFontTemplates.libertine).next_to(UP*2,RIGHT).set_opacity(0.3)
        lbl_x1 = Tex(r'$-1$', tex_template = TexFontTemplates.libertine).next_to(LEFT,DR*0.2,aligned_edge = LEFT).scale(0.7).set_opacity(0.7).set_z_index(1)
        lbl_x2 = Tex(r'$1$', tex_template = TexFontTemplates.libertine).next_to(RIGHT,DR*0.2,aligned_edge = LEFT).shift(RIGHT*0.1).scale(0.7).set_opacity(0.7).set_z_index(1)
        lbl_y1 = Tex(r'$-1$', tex_template = TexFontTemplates.libertine).next_to(DOWN,UR*0.2,aligned_edge = LEFT).scale(0.7).set_opacity(0.7).set_z_index(1)
        lbl_y2 = Tex(r'$1$', tex_template = TexFontTemplates.libertine).next_to(UP,UR*0.2,aligned_edge = LEFT).shift(RIGHT*0.1).scale(0.7).set_opacity(0.7).set_z_index(1)

        self.play(Create(rectPlane, run_time=3, lag_ratio=0.1))
        self.play(
            FadeIn(lbl_x_axis),
            FadeIn(lbl_y_axis)
        )
        self.play(Create(square_1))
        self.play(
            FadeIn(lbl_x1),
            FadeIn(lbl_x2),
            FadeIn(lbl_y1),
            FadeIn(lbl_y2)
        )
        self.wait(2)

        self.play(
            FadeOut(rectPlane),
            FadeOut(lbl_x_axis),
            FadeOut(lbl_y_axis),
            FadeOut(lbl_x1),
            FadeOut(lbl_x2),
            FadeOut(lbl_y1),
            FadeOut(lbl_y2)
        )

        header_mini = Tex(r'$z$',r'$\,\rightarrow\,$',r'$e^z$', tex_template = TexFontTemplates.libertine).scale(1.5).to_edge(UL*1.5).set_z_index(1)
        header_mini[0].set_color(TEAL_C)
        header_mini[2].set_color(PURPLE_C)

        self.play(
            ApplyMethod(header_math.become,header_mini),
            FadeOut(header[0], target_position = header_mini, scale = 0.5),
            FadeOut(header[-1], target_position = header_mini, scale = 0.5)
        )

        polarPlane = PolarPlane(radius_max = 8).set_opacity(0.3).set_fill(opacity=0)
        line_a1 = Line(ORIGIN, polarPlane.polar_to_point(4,1),stroke_width=2).set_opacity(0.3).set_z_index(1)
        line_a2 = Line(ORIGIN, polarPlane.polar_to_point(4,TAU-1),stroke_width=2).set_opacity(0.3).set_z_index(1)
        lbl_a1 = Tex(r'$1$ rad', tex_template = TexFontTemplates.libertine).move_to(line_a1.get_end()+UP*0.2).scale(0.7).set_opacity(0.7).set_z_index(1)
        lbl_a2 = Tex(r'$-1$ rad', tex_template = TexFontTemplates.libertine).move_to(line_a2.get_end()+DOWN*0.2).scale(0.7).set_opacity(0.7).set_z_index(1)
        lbl_r1 = Tex(r'$e^{-1}$', tex_template = TexFontTemplates.libertine).move_to(polarPlane.polar_to_point(np.exp(-1),0)+DOWN*0.2+RIGHT*0.3).scale(0.7).set_opacity(0.7).set_z_index(1)
        lbl_r2 = Tex(r'$e^1$', tex_template = TexFontTemplates.libertine).move_to(polarPlane.polar_to_point(np.exp(1),0)+DOWN*0.2+RIGHT*0.1).scale(0.7).set_opacity(0.7).set_z_index(1)

        lbl_y_axis.next_to(UP*3,RIGHT)
        self.play(Create(polarPlane), run_time=3, lag_ratio=0.1)
        self.play(
            FadeIn(lbl_x_axis),
            FadeIn(lbl_y_axis)
        )

        def expZTransform(mobject):
            mobject.apply_complex_function(lambda z: np.exp(z)) #lambda z: np.exp(z)-np.exp((z-z.conjugate())/2) Convierte el primer cuadrante en un circulo
            mobject.set_color(PURPLE_C)
            return mobject

        self.play(ApplyFunction(expZTransform,square_1), run_time = 2)
        self.play(
            Create(line_a1),
            Create(line_a2),
            FadeIn(lbl_a1),
            FadeIn(lbl_a2),
            FadeIn(lbl_r1),
            FadeIn(lbl_r2)
        )
        self.wait(2)
        self.play(
            FadeOut(line_a1),
            FadeOut(line_a2),
            FadeOut(lbl_x_axis),
            FadeOut(lbl_y_axis),
            FadeOut(lbl_a1),
            FadeOut(lbl_a2),
            FadeOut(lbl_r1),
            FadeOut(lbl_r2),
            FadeOut(polarPlane),
            FadeOut(square_1),
            FadeOut(header_math)
        )

class ExpZ_2(Scene):
    def construct(self):

        ##------------------------------
        ## Logo LME en la esquina
        ##------------------------------
        brand = Text(
            "LED Me Explain",
            fill_opacity = 0.5,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_color,"[3:4]":LME_color,"[5:6]":LME_color} ## Los espacios no cuentan como caracteres
        ).scale(0.4).to_edge(DR)
        # Añade el logo
        self.add(brand)
        ##---------------------------------
        ##---------------------------------

        ##------------------------------
        ## 2. Desarrollo Matemático
        ##------------------------------

        text_1 = Tex('Expresamos la variable ',r'$z$',' en coordenadas cartesianas').to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-2)
        text_1_math = MathTex(r'z', tex_template = TexFontTemplates.libertine).move_to(text_1[1]).scale(1.3)
        text_1_math.set_color_by_tex('z',TEAL_C)

        eq_1 = MathTex(r'z',r'=',r'x',r'+',r'i',r'y',tex_template = TexFontTemplates.libertine).scale(2)
        eq_1.set_color_by_tex(r'z',TEAL_C)
        eq_1.set_color_by_tex(r'x',GREEN)
        eq_1.set_color_by_tex(r'y',RED)

        self.play(
            Write(text_1),
            FadeOut(text_1[1]),
            FadeIn(text_1_math),
            run_time = 0.8
        )
        self.wait()
        self.play(FadeIn(eq_1))
        self.wait()
        self.play(
            Unwrite(text_1),
            FadeOut(text_1_math),
            run_time = 0.7
        )

        text_2 = Tex('Y la variable ',r'$w$',r' como la transformación').to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-2)
        text_2_math = MathTex(r'w', tex_template = TexFontTemplates.libertine).move_to(text_2[1]).scale(1.5)
        text_2_math.set_color_by_tex(r'w',PURPLE_C)

        eq_2 = MathTex(r'w',r'=',r'e^',r'z',tex_template = TexFontTemplates.libertine).scale(2).next_to(eq_1,aligned_edge = UP)
        eq_2.set_color_by_tex(r'z',TEAL_C)
        eq_2.set_color_by_tex(r'w',PURPLE_C)

        self.play(
            Write(text_2),
            FadeOut(text_2[1]),
            FadeIn(text_2_math),
            run_time = 0.8
        )
        self.wait()
        self.play(ApplyMethod(eq_1.shift,LEFT*3))
        self.play(FadeIn(eq_2))
        self.wait()
        self.play(
            Unwrite(text_2),
            FadeOut(text_2_math),
            run_time = 0.7
        )

        text_3 = Tex('Resolvemos la transformación: ',r'$w=u(x,y)+i\,v(x,y)$').to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-2)
        text_3_math = MathTex(r'w',r'=',r'u(x,y)',r'+',r'i\,',r'v(x,y)', tex_template = TexFontTemplates.libertine).move_to(text_3[1]).scale(1.2)
        text_3_math.set_color_by_tex(r'w',PURPLE_C)
        text_3_math.set_color_by_tex(r'u',GREEN)
        text_3_math.set_color_by_tex(r'v',RED)

        eq_3 = MathTex(r'w',r'=',r'e^{',r'x',r'+',r'i',r'y}',tex_template = TexFontTemplates.libertine).scale(2).move_to(eq_2,aligned_edge = LEFT)
        eq_3.set_color_by_tex(r'x',GREEN)
        eq_3.set_color_by_tex(r'y',RED)
        eq_3.set_color_by_tex(r'w',PURPLE_C)

        self.play(
            Write(text_3),
            FadeOut(text_3[1]),
            FadeIn(text_3_math),
            run_time = 0.8
        )
        self.wait()
        self.play(
            Indicate(eq_1[0]),
            Indicate(eq_2[3]),
            run_time = 1.5
        )
        self.wait()
        self.play(
            TransformMatchingShapes(eq_2,eq_3),
            FadeOut(eq_1[0:2]),
            FadeOut(eq_1[2:], target_position = eq_3[5])
        )
        self.play(ApplyMethod(eq_3.move_to,ORIGIN))
        self.wait()

        eq_3_hint = MathTex(r'\text{** Por Leyes de los Exponentes: }',r'a',r'^{b',r'+',r'c}',r'=',r'a',r'^b',r'a',r'^c',tex_template = TexFontTemplates.comfortaa).next_to(eq_3,DOWN*1.5).scale(0.8)
        eq_3_hint.set_color_by_tex('b',LIGHT_PINK)
        eq_3_hint.set_color_by_tex('c',YELLOW)

        self.play(FadeIn(eq_3_hint, target_position = eq_3))
        self.wait()

        eq_4 = MathTex(r'w',r'=',r'e^',r'x',r'e^{',r'i',r'y}',tex_template = TexFontTemplates.libertine).scale(2)

        eq_4[2:4].set_color(LIGHT_PINK)
        eq_4.set_color_by_tex(r'y',YELLOW)
        eq_4.set_color_by_tex(r'w',PURPLE_C)


        self.play(TransformMatchingShapes(eq_3,eq_4))
        self.wait()

        eq_4_rect = SurroundingRectangle(eq_4, ORANGE, buff = 0.3)
        eq_4_rect_txt = Text('Forma polar', color = ORANGE).scale(0.6).next_to(eq_4_rect,UP)

        self.play(Create(eq_4_rect))
        self.play(Write(eq_4_rect_txt), run_time = 0.8)
        self.wait(2)
        self.play(
        FadeOut(eq_3_hint),
        FadeOut(eq_4_rect),
        FadeOut(eq_4_rect_txt)
        )
        self.wait()

        eq_4_hint = MathTex(r'\text{** Por Fórmula de Euler: }',r'r',r'e',r'^{i\,',r'\theta}',r'=',r'r',r'\cos(',r'\theta',r')',r'+',r'i\,',r'r',r'\sin(',r'\theta',r')',tex_template = TexFontTemplates.comfortaa).next_to(eq_4,DOWN*1.5).scale(0.8)
        eq_4_hint.set_color_by_tex('r',LIGHT_PINK)
        eq_4_hint[0].set_color(WHITE)
        eq_4_hint.set_color_by_tex(r'\theta',YELLOW_D)

        self.play(FadeIn(eq_4_hint, target_position = eq_4))
        self.wait()

        eq_5 = MathTex(r'w',r'=',r'e^x',r'\cos(',r'y',r')',r'+',r'i\,',r'e^x',r'\sin(',r'y',r')',tex_template = TexFontTemplates.libertine).scale(2)
        eq_5.set_color_by_tex(r'w',PURPLE_C)
        eq_5.set_color_by_tex(r'e^x',LIGHT_PINK)
        eq_5.set_color_by_tex(r'y',YELLOW)

        self.play(
            TransformMatchingShapes(eq_4[0:2],eq_5[0:2]),
            TransformMatchingShapes(eq_4[2:4],eq_5[2:3]),
            TransformMatchingShapes(eq_4[2:4].copy(),eq_5[8:9]),
            FadeOut(eq_4[4]),
            TransformMatchingShapes(eq_4[5:6],eq_5[7:8]),
            TransformMatchingShapes(eq_4[6:7],eq_5[3:6]),
            TransformMatchingShapes(eq_4[6:7].copy(),eq_5[9:12]),
            FadeIn(eq_5[6])
        )
        self.wait()

        eq_5_rect = SurroundingRectangle(eq_5, TEAL_C, buff = 0.3)
        eq_5_rect_txt = Text('Forma cartesiana', color = TEAL_C).scale(0.6).next_to(eq_5_rect,UP)

        self.play(Create(eq_5_rect))
        self.play(Write(eq_5_rect_txt), run_time = 0.8)
        self.wait(2)

        eq_6 = MathTex(r'w',r'=',r'e^x\cos(y)',r'+',r'i\,',r'e^x\sin(y)',tex_template = TexFontTemplates.libertine).scale(2)
        eq_6.set_color_by_tex(r'w',PURPLE_C)
        eq_6.set_color_by_tex(r'\cos',GREEN)
        eq_6.set_color_by_tex(r'\sin',RED)

        self.play(
            FadeOut(text_3_math[2].copy(), target_position = eq_6[2]),
            FadeOut(text_3_math[5].copy(), target_position = eq_6[5]),
            FadeOut(eq_5),
            FadeIn(eq_6)
        )
        self.wait(2)

        self.play(
            FadeOut(text_3[0]),
            FadeOut(text_3_math),
            FadeOut(eq_5_rect_txt),
            FadeOut(eq_5_rect),
            FadeOut(eq_4_hint)
        )

        text_4 = Tex('Por simplicidad, usaremos la forma polar de ',r'$w$').to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-2)
        text_4_math = MathTex(r'w', tex_template = TexFontTemplates.libertine).move_to(text_4[1]).scale(1.3)
        text_4_math.set_color_by_tex(r'w',PURPLE_C)

        self.play(
            Write(text_4),
            FadeOut(text_4[1]),
            FadeIn(text_4_math),
            run_time = 0.8
        )
        self.play(ApplyMethod(eq_6.shift,DOWN*2))
        self.play(FadeIn(eq_4))
        self.wait()
        self.play(Unwrite(eq_6), run_time = 0.7)
        self.wait()
        self.play(
            Unwrite(text_4),
            FadeOut(text_4_math),
            run_time = 0.7
        )
        self.wait()

        ##---------------------------------
        ##---------------------------------

class ExpZ_3(Scene):
    def construct(self):

        ##------------------------------
        ## Logo LME en la esquina
        ##------------------------------
        brand = Text(
            "LED Me Explain",
            fill_opacity = 0.5,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_color,"[3:4]":LME_color,"[5:6]":LME_color} ## Los espacios no cuentan como caracteres
        ).scale(0.4).to_edge(DR)
        # Añade el logo
        self.add(brand)
        ##---------------------------------
        ##---------------------------------

        ##------------------------------
        ## 3. Recordatorio de complejos en forma polar
        ##------------------------------

        text_1 = Tex('Pero... ¿Cómo se ve un número complejo en forma polar?').to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-2)

        eq_1 = MathTex(r'w',r'=',r'e^',r'x',r'e^{',r'i',r'y}',tex_template = TexFontTemplates.libertine).scale(2).set_z_index(1)

        eq_1[2:4].set_color(LIGHT_PINK)
        eq_1.set_color_by_tex(r'y',YELLOW)
        eq_1.set_color_by_tex(r'w',PURPLE_C)

        self.add(eq_1) # Inicio de la escena

        self.play(FadeIn(text_1))
        self.wait(2)

        def eq_mini_UL(mobject):
            mobject.scale(0.6)
            mobject.to_edge(UL)
            mobject.set_opacity(0.5)
            return mobject

        self.play(
            ApplyFunction(eq_mini_UL,eq_1),
            FadeOut(text_1)
        )
        self.wait()

        eq_2 = MathTex(r'w_{prueba}',r'=',r'r',r'e^{',r'i\,',r'\theta}').scale(1.5).to_edge(UP).set_z_index(1)

        eq_2[2].set_color(LIGHT_PINK)
        eq_2[5].set_color(YELLOW)
        eq_2[0].set_color(PURPLE_C)

        self.play(Write(eq_2))

        polarPlane = PolarPlane(radius_max = 13).set_opacity(0.3).set_fill(opacity=0).shift(DOWN*2)
        RIGHT_line_polarPlane = Line(polarPlane.polar_to_point(0,0), polarPlane.polar_to_point(0,0)+RIGHT)
        ORIGIN_polarPlane = polarPlane.polar_to_point(0,0)

        lbl_x_axis = MathTex(r'Re', tex_template = TexFontTemplates.libertine).next_to(ORIGIN_polarPlane+RIGHT*6,UP).set_opacity(0.3)
        lbl_y_axis = MathTex(r'Im', tex_template = TexFontTemplates.libertine).next_to(ORIGIN_polarPlane+UP*4,RIGHT).set_opacity(0.3)

        self.play(Create(polarPlane), run_time=3, lag_ratio=0.1)
        self.play(
            FadeIn(lbl_x_axis),
            FadeIn(lbl_y_axis)
        )
        self.wait()

        r_w_p = Variable(3, r'r', num_decimal_places=2).set_z_index(1)
        r_w_p.value.set_color(LIGHT_PINK)

        a_w_p = Variable(PI/4, r'\theta', num_decimal_places=2).set_z_index(1)
        a_w_p.value.set_color(YELLOW)


        def eq_2_updater(mobject):
            mobject.become(MathTex(r'w_{prueba}',r'=',"{0:.2f}".format(r_w_p.tracker.get_value()),r'e^{',r'i\,',"{0:.2f}".format(a_w_p.tracker.get_value())).scale(1.5).to_edge(UP).set_z_index(1))
            mobject[2].set_color(LIGHT_PINK)
            mobject[5].set_color(YELLOW)
            mobject[0].set_color(PURPLE_C)
            return mobject

        eq_2_values = MathTex(r'w_{prueba}',r'=',"{0:.2f}".format(r_w_p.tracker.get_value()),r'e^{',r'i\,',"{0:.2f}".format(a_w_p.tracker.get_value())).scale(1.5).to_edge(UP).set_z_index(1)
        eq_2_values[2].set_color(LIGHT_PINK)
        eq_2_values[5].set_color(YELLOW)
        eq_2_values[0].set_color(PURPLE_C)

        line_w_p = DashedLine(ORIGIN_polarPlane, polarPlane.polar_to_point(r_w_p.tracker.get_value(),a_w_p.tracker.get_value()),stroke_width=3, dash_length = 0.1, dash_spacing = 0.1).set_color(LIGHT_PINK).set_z_index(1)
        def line_w_p_updater(mobject):
            mobject.become(
                DashedLine(ORIGIN_polarPlane, polarPlane.polar_to_point(r_w_p.tracker.get_value(),a_w_p.tracker.get_value()),stroke_width=3, dash_length = 0.1, dash_spacing = 0.1).set_color(LIGHT_PINK).set_z_index(1)
            )
            return mobject

        line_w_p_lbl_init = MathTex(r'r').scale(0.8).move_to(
            Line(
                ORIGIN_polarPlane+UL*.2, polarPlane.polar_to_point(r_w_p.tracker.get_value(),a_w_p.tracker.get_value())+UL*.2,stroke_width=3
            ).get_midpoint(), aligned_edge = RIGHT
        ).set_color(LIGHT_PINK)
        line_w_p_lbl = r_w_p.copy().value.scale(0.8).move_to(
            Line(
                ORIGIN_polarPlane+UL*.2, polarPlane.polar_to_point(r_w_p.tracker.get_value(),a_w_p.tracker.get_value())+UL*.2,stroke_width=3
            ).get_midpoint(), aligned_edge = RIGHT
        )
        def line_w_p_lbl_updater(mobject):
            mobject.move_to(
                Line(
                    ORIGIN_polarPlane+UL*.2, polarPlane.polar_to_point(r_w_p.tracker.get_value(),a_w_p.tracker.get_value())+UL*.2,stroke_width=3
                ).get_midpoint(), aligned_edge = RIGHT
            )
            return mobject

        angle_w_p = Angle(RIGHT_line_polarPlane, line_w_p, radius=0.5, other_angle=False).set_color(YELLOW).set_z_index(1)
        def angle_w_p_updater(mobject):
            mobject.become(
                Angle(RIGHT_line_polarPlane, line_w_p, radius=0.5, other_angle=False).set_color(YELLOW).set_z_index(1)
            )
            return mobject


        angle_w_p_lbl_init = MathTex(r'\theta').scale(0.8).move_to(
            Angle(
                RIGHT_line_polarPlane, line_w_p, radius=1, other_angle=False
            ).get_midpoint()
        ).set_color(YELLOW)
        angle_w_p_lbl = a_w_p.copy().value.scale(0.8).move_to(
            Angle(
                RIGHT_line_polarPlane, line_w_p, radius=1, other_angle=False
            ).get_midpoint()
        )
        def angle_w_p_lbl_updater(mobject):
            mobject.move_to(
                Angle(
                    RIGHT_line_polarPlane, line_w_p, radius=1, other_angle=False
                ).get_midpoint()
            )
            return mobject

        dot_w_p = Dot(polarPlane.polar_to_point(r_w_p.tracker.get_value(),a_w_p.tracker.get_value()),radius=.1,color=PURPLE_C).set_z_index(2)
        def dot_w_p_updater(mobject):
            mobject.move_to(
                polarPlane.polar_to_point(r_w_p.tracker.get_value(),a_w_p.tracker.get_value())
            )
            return mobject

        dot_w_p_lbl = MathTex('w_{prueba}').set_color(PURPLE_C).next_to(dot_w_p).set_z_index(2)
        def dot_w_p_lbl_updater(mobject):
            mobject.next_to(dot_w_p)
            return mobject



        self.play(
            FadeIn(dot_w_p),
            FadeIn(dot_w_p_lbl)
        )
        self.wait()
        self.play(Create(line_w_p))
        self.play(FadeIn(line_w_p_lbl_init, target_position = eq_2[2]))
        self.play(Create(angle_w_p))
        self.play(FadeIn(angle_w_p_lbl_init, target_position = eq_2[5]))
        self.wait()
        self.play(
            FadeOut(eq_2, shift=DOWN),
            FadeIn(eq_2_values, shift=DOWN)
        )
        self.play(
            FadeOut(line_w_p_lbl_init),
            FadeIn(line_w_p_lbl, target_position = eq_2_values[2])
        )
        self.play(
            FadeOut(angle_w_p_lbl_init),
            FadeIn(angle_w_p_lbl, target_position = eq_2_values[5])
        )
        self.wait()

        eq_2_values.add_updater(eq_2_updater)
        line_w_p.add_updater(line_w_p_updater)
        line_w_p_lbl.add_updater(line_w_p_lbl_updater)
        dot_w_p.add_updater(dot_w_p_updater)
        dot_w_p_lbl.add_updater(dot_w_p_lbl_updater)
        angle_w_p.add_updater(angle_w_p_updater)
        angle_w_p_lbl.add_updater(angle_w_p_lbl_updater)

        self.play(r_w_p.tracker.animate.set_value(5))
        self.wait(0.5)
        self.play(a_w_p.tracker.animate.set_value(2*PI/3))
        self.wait(0.5)
        self.play(r_w_p.tracker.animate.set_value(2))
        self.wait(0.5)
        self.play(a_w_p.tracker.animate.set_value(PI/6))
        self.wait(0.5)
        self.play(r_w_p.tracker.animate.set_value(3))
        self.wait(0.5)
        self.play(a_w_p.tracker.animate.set_value(PI/4))
        self.wait()

        eq_2_values.remove_updater(eq_2_updater)
        line_w_p.remove_updater(line_w_p_updater)
        line_w_p_lbl.remove_updater(line_w_p_lbl_updater)
        dot_w_p.remove_updater(dot_w_p_updater)
        dot_w_p_lbl.remove_updater(dot_w_p_lbl_updater)
        angle_w_p.remove_updater(angle_w_p_updater)
        angle_w_p_lbl.remove_updater(angle_w_p_lbl_updater)

        self.wait()

        self.play(
            FadeOut(polarPlane),
            FadeOut(lbl_x_axis),
            FadeOut(lbl_y_axis),
            FadeOut(line_w_p),
            FadeOut(line_w_p_lbl),
            FadeOut(angle_w_p),
            FadeOut(angle_w_p_lbl),
            FadeOut(dot_w_p),
            FadeOut(dot_w_p_lbl),
            FadeOut(eq_2_values)
        )

        def eq_max_ORIGIN(mobject):
            mobject.scale(10/6)
            mobject.move_to(ORIGIN)
            mobject.set_opacity(1)
            return mobject

        self.play(ApplyFunction(eq_max_ORIGIN,eq_1))
        self.wait()

class ExpZ_4(Scene):
    def construct(self):

        ##------------------------------
        ## Logo LME en la esquina
        ##------------------------------
        brand = Text(
            "LED Me Explain",
            fill_opacity = 0.5,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_color,"[3:4]":LME_color,"[5:6]":LME_color} ## Los espacios no cuentan como caracteres
        ).scale(0.4).to_edge(DR)
        # Añade el logo
        self.add(brand)
        ##---------------------------------
        ##---------------------------------

        ##------------------------------
        ## 4. Desarrollo gráfico de la transformación
        ##------------------------------

        text_1 = Tex('Ahora... ¿Qué pasa al aplicar la transformación?').to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-2)

        eq_1 = MathTex(r'w',r'=',r'e^',r'x',r'e^{',r'i',r'y}',tex_template = TexFontTemplates.libertine).scale(2).set_z_index(2)
        eq_1[2:4].set_color(LIGHT_PINK)
        eq_1.set_color_by_tex(r'y',YELLOW)
        eq_1.set_color_by_tex(r'w',PURPLE_C)

        eq_2 = MathTex(r'z',r'=',r'x',r'+',r'i',r'y',tex_template = TexFontTemplates.libertine).next_to(eq_1,LEFT,aligned_edge = DOWN).scale(2).set_z_index(2)
        eq_2.set_color_by_tex(r'z',TEAL_C)
        eq_2.set_color_by_tex(r'x',GREEN)
        eq_2.set_color_by_tex(r'y',RED)

        eq_3 = MathTex(r'\longrightarrow',tex_template = TexFontTemplates.libertine).scale(2).set_z_index(2)
        eq_4 = MathTex(r'e^z',tex_template = TexFontTemplates.libertine).scale(1.5).shift(UP*.5).set_z_index(2)
        trans_group = VGroup(eq_3,eq_4)

        self.add(eq_1) # Inicio de la escena
        self.play(Write(text_1), run_time = 0.8)
        self.wait()
        self.play(
            eq_1.animate.shift(RIGHT*3),
            FadeIn(eq_2, target_position = ORIGIN)
        )
        self.play(Write(trans_group), run_time = 0.8)
        self.wait(2)

        self.play(Unwrite(text_1), run_time = 0.7)

        def eq_1_anim(mobject):
            mobject.move_to(RIGHT*3.5+UP*3.4)
            mobject[1:].set_color(WHITE)
            mobject.scale(0.8)
            return mobject

        def eq_2_anim(mobject):
            mobject.move_to(LEFT*3.5+UP*3.2)
            mobject[1:].set_color(WHITE)
            mobject.scale(0.8)
            return mobject

        def eq_trans_anim(mobject):
            mobject.to_edge(UP)
            mobject.scale(0.8)
            return mobject

        self.play(
            ApplyFunction(eq_1_anim,eq_1),
            ApplyFunction(eq_2_anim,eq_2),
            ApplyFunction(eq_trans_anim,trans_group)
        )

        rectPlane = NumberPlane(x_range=(-3, 3, 1), y_range=(-3, 3, 1)).set_opacity(0.3).shift(LEFT*3.5)
        rect_x_axis = MathTex(r'Re', tex_template = TexFontTemplates.libertine).next_to(LEFT*3.5+RIGHT*2.5,UP).set_opacity(0.3)
        rect_y_axis = MathTex(r'Im', tex_template = TexFontTemplates.libertine).next_to(LEFT*3.5+UP*2.5,RIGHT).set_opacity(0.3)

        rectPlaneGroup = Group(rectPlane,rect_x_axis,rect_y_axis)

        polarPlane = PolarPlane(radius_max = 3).set_opacity(0.3).set_fill(opacity=0).shift(RIGHT*3.5)
        polar_x_axis = rect_x_axis.copy().next_to(RIGHT*3.5+RIGHT*2.5,UP)
        polar_y_axis = rect_y_axis.copy().next_to(RIGHT*3.5+UP*2.5,RIGHT)

        polarPlaneGroup = Group(polarPlane,polar_x_axis,polar_y_axis)

        self.play(
            Create(polarPlane),
            Create(rectPlane),
            FadeIn(rect_x_axis),
            FadeIn(rect_y_axis),
            FadeIn(polar_x_axis),
            FadeIn(polar_y_axis),
            run_time=3,
            lag_ratio=0.1
        )
        self.wait()

        def expZTransform(z):
            z = np.exp(z) #lambda z: np.exp(z)-np.exp((z-z.conjugate())/2) Convierte el primer cuadrante en un circulo
            return z

        line_rect_1 = Line(rectPlane.coords_to_point(-1,1),rectPlane.coords_to_point(1,1)).set_color(TEAL_C).set_z_index(1)
        line_rect_2 = Line(rectPlane.coords_to_point(1,1),rectPlane.coords_to_point(1,-1)).set_color(TEAL_C).set_z_index(1)
        line_rect_3 = Line(rectPlane.coords_to_point(1,-1),rectPlane.coords_to_point(-1,-1)).set_color(TEAL_C).set_z_index(1)
        line_rect_4 = Line(rectPlane.coords_to_point(-1,-1),rectPlane.coords_to_point(-1,1)).set_color(TEAL_C).set_z_index(1)
        dot_rect_1 = Dot(line_rect_1.get_start()).scale(0.8).set_color(YELLOW_D).set_z_index(2)
        dot_rect_2 = Dot(line_rect_2.get_start()).scale(0.8).set_color(GREEN).set_z_index(2)
        dot_rect_3 = Dot(line_rect_3.get_start()).scale(0.8).set_color(BLUE).set_z_index(2)
        dot_rect_4 = Dot(line_rect_4.get_start()).scale(0.8).set_color(RED_B).set_z_index(2)
        dot_rect_1_lbl = MathTex('z_1').scale(0.8).set_opacity(0.7).next_to(dot_rect_1,LEFT).set_z_index(2)
        dot_rect_2_lbl = MathTex('z_2').scale(0.8).set_opacity(0.7).next_to(dot_rect_2,RIGHT).set_z_index(2)
        dot_rect_3_lbl = MathTex('z_3').scale(0.8).set_opacity(0.7).next_to(dot_rect_3,RIGHT).set_z_index(2)
        dot_rect_4_lbl = MathTex('z_4').scale(0.8).set_opacity(0.7).next_to(dot_rect_4,LEFT).set_z_index(2)

        line_rect = Group(line_rect_1,line_rect_2,line_rect_3,line_rect_4)
        dot_rect = Group(dot_rect_1,dot_rect_2,dot_rect_3,dot_rect_4)
        dot_rect_lbl = Group(dot_rect_1_lbl,dot_rect_2_lbl,dot_rect_3_lbl,dot_rect_4_lbl)

        line_polar_1 = Line([-1,1,0],[1,1,0]).set_color(PURPLE_C).set_z_index(1)
        line_polar_1.apply_complex_function(expZTransform).shift(RIGHT*3.5)
        line_polar_2 = Line([1,1,0],[1,-1,0]).set_color(PURPLE_C).set_z_index(1)
        line_polar_2.apply_complex_function(expZTransform).shift(RIGHT*3.5)
        line_polar_3 = Line([1,-1,0],[-1,-1,0]).set_color(PURPLE_C).set_z_index(1)
        line_polar_3.apply_complex_function(expZTransform).shift(RIGHT*3.5)
        line_polar_4 = Line([-1,-1,0],[-1,1,0]).set_color(PURPLE_C).set_z_index(1)
        line_polar_4.apply_complex_function(expZTransform).shift(RIGHT*3.5)
        dot_polar_1 = Dot(line_polar_1.get_start()).scale(0.8).set_color(YELLOW_D).set_z_index(2)
        dot_polar_2 = Dot(line_polar_2.get_start()).scale(0.8).set_color(GREEN).set_z_index(2)
        dot_polar_3 = Dot(line_polar_3.get_start()).scale(0.8).set_color(BLUE).set_z_index(2)
        dot_polar_4 = Dot(line_polar_4.get_start()).scale(0.8).set_color(RED_B).set_z_index(2)
        dot_polar_1_lbl = MathTex('w_1').scale(0.8).set_opacity(0.7).next_to(dot_polar_1,RIGHT).set_z_index(2)
        dot_polar_2_lbl = MathTex('w_2').scale(0.8).set_opacity(0.7).next_to(dot_polar_2,RIGHT).set_z_index(2)
        dot_polar_3_lbl = MathTex('w_3').scale(0.8).set_opacity(0.7).next_to(dot_polar_3,RIGHT).set_z_index(2)
        dot_polar_4_lbl = MathTex('w_4').scale(0.8).set_opacity(0.7).next_to(dot_polar_4,RIGHT).set_z_index(2)

        line_polar = Group(line_polar_1,line_polar_2,line_polar_3,line_polar_4)
        dot_polar = Group(dot_polar_1,dot_polar_2,dot_polar_3,dot_polar_4)
        dot_polar_lbl = Group(dot_polar_1_lbl,dot_polar_2_lbl,dot_polar_3_lbl,dot_polar_4_lbl)

        eq_rect_1 = MathTex('z_1=-1+i\,1').set_color(YELLOW_D).set_z_index(2)
        eq_rect_2 = MathTex('z_2=1+i\,1').set_color(GREEN).set_z_index(2)
        eq_rect_3 = MathTex('z_3=1-i\,1').set_color(BLUE).set_z_index(2)
        eq_rect_4 = MathTex('z_4=-1-i\,1').set_color(RED_B).set_z_index(2)

        eq_rect = Group(eq_rect_1,eq_rect_2,eq_rect_4,eq_rect_3)

        eq_rect.arrange_in_grid(rows=2, cols=2, row_alignments='uu', col_aligments = 'll', buff=0.5).move_to(rectPlane).shift(DOWN*2.5)

        eq_polar_1 = MathTex('w_1=e^{-1}e^{i\,1}').set_color(YELLOW_D).set_z_index(2)
        eq_polar_2 = MathTex('w_2=e^1e^{i\,1}').set_color(GREEN).set_z_index(2)
        eq_polar_3 = MathTex('w_3=e^1e^{-i\,1}').set_color(BLUE).set_z_index(2)
        eq_polar_4 = MathTex('w_4=e^{-1}e^{-i\,1}').set_color(RED_B).set_z_index(2)

        eq_polar = Group(eq_polar_1,eq_polar_2,eq_polar_3,eq_polar_4)

        eq_polar.arrange_in_grid(rows=4, cols=1, cell_alignment = LEFT, buff=0.5).move_to(polarPlane).shift(LEFT*1.5)

        self.play(
            FadeIn(dot_rect_1),
            FadeIn(dot_rect_1_lbl),
            FadeIn(eq_rect_1, target_position = dot_rect_1),
            FadeIn(dot_polar_1),
            FadeIn(dot_polar_1_lbl),
            FadeIn(eq_polar_1, target_position = dot_polar_1)
        )

        self.wait()
        self.play(
            Create(line_rect_1),
            Create(line_polar_1),
            run_time = 2
        )

        self.play(
            FadeIn(dot_rect_2),
            FadeIn(dot_rect_2_lbl),
            FadeIn(eq_rect_2, target_position = dot_rect_2),
            FadeIn(dot_polar_2),
            FadeIn(dot_polar_2_lbl),
            FadeIn(eq_polar_2, target_position = dot_polar_2)
        )

        self.wait()
        self.play(
            Create(line_rect_2),
            Create(line_polar_2),
            run_time = 2
        )

        self.play(
            FadeIn(dot_rect_3),
            FadeIn(dot_rect_3_lbl),
            FadeIn(eq_rect_3, target_position = dot_rect_3),
            FadeIn(dot_polar_3),
            FadeIn(dot_polar_3_lbl),
            FadeIn(eq_polar_3, target_position = dot_polar_3)
        )

        self.wait()
        self.play(
            Create(line_rect_3),
            Create(line_polar_3),
            run_time = 2
        )

        self.play(
            FadeIn(dot_rect_4),
            FadeIn(dot_rect_4_lbl),
            FadeIn(eq_rect_4, target_position = dot_rect_4),
            FadeIn(dot_polar_4),
            FadeIn(dot_polar_4_lbl),
            FadeIn(eq_polar_4, target_position = dot_polar_4)
        )

        self.wait()
        self.play(
            Create(line_rect_4),
            Create(line_polar_4),
            run_time = 2
        )

        self.wait(2)

        self.play(
            FadeOut(eq_polar),
            FadeOut(line_polar),
            FadeOut(dot_polar),
            FadeOut(dot_polar_lbl),
            FadeOut(eq_rect),
            FadeOut(line_rect),
            FadeOut(dot_rect),
            FadeOut(dot_rect_lbl),
            FadeOut(polarPlaneGroup),
            FadeOut(rectPlaneGroup)
        )
        self.wait()

class ExpZ_5(Scene):
    def construct(self):
        ##------------------------------
        ## Logo LME en la esquina
        ##------------------------------
        brand = Text(
            "LED Me Explain",
            fill_opacity = 0.5,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_color,"[3:4]":LME_color,"[5:6]":LME_color} ## Los espacios no cuentan como caracteres
        ).scale(0.4).to_edge(DR)
        # Añade el logo
        self.add(brand)
        ##---------------------------------
        ##---------------------------------

        ##------------------------------
        ## 5. Otros ejemplos de la transformación
        ##------------------------------

        eq_1 = MathTex(r'w',r'=',r'e^',r'x',r'e^{',r'i',r'y}',tex_template = TexFontTemplates.libertine).scale(1.6).move_to(RIGHT*3.5+UP*3.4).set_z_index(2)
        eq_1.set_color_by_tex(r'w',PURPLE_C)

        eq_2 = MathTex(r'z',r'=',r'x',r'+',r'i',r'y',tex_template = TexFontTemplates.libertine).move_to(LEFT*3.5+UP*3.2).scale(1.6).set_z_index(2)
        eq_2.set_color_by_tex(r'z',TEAL_C)

        eq_3 = MathTex(r'\longrightarrow',tex_template = TexFontTemplates.libertine).scale(2).set_z_index(2)
        eq_4 = MathTex(r'e^z',tex_template = TexFontTemplates.libertine).scale(1.5).shift(UP*.5).set_z_index(2)
        eq_trans = Group(eq_3,eq_4).to_edge(UP).scale(0.8)

        eq_group = Group(eq_1,eq_2,eq_trans)

        self.add(eq_group) # Ecuaciones iniciales

        text_1 = Tex('¿Y si transformamos una trayectoria diferente?').scale_to_fit_width(config["frame_width"]-2)

        self.play(Write(text_1), run_time = 0.8)
        self.wait(2.5)
        self.play(Unwrite(text_1), run_time = 0.7)

        rectPlane = NumberPlane(x_range=(-3, 3, 1), y_range=(-3, 3, 1)).set_opacity(0.3).shift(LEFT*3.5)
        rect_x_axis = MathTex(r'Re', tex_template = TexFontTemplates.libertine).next_to(LEFT*3.5+RIGHT*2.5,UP).set_opacity(0.3)
        rect_y_axis = MathTex(r'Im', tex_template = TexFontTemplates.libertine).next_to(LEFT*3.5+UP*2.5,RIGHT).set_opacity(0.3)

        rectPlaneGroup = Group(rectPlane,rect_x_axis,rect_y_axis)

        polarPlane = PolarPlane(radius_max = 3).set_opacity(0.3).set_fill(opacity=0).shift(RIGHT*3.5)
        polar_x_axis = rect_x_axis.copy().next_to(RIGHT*3.5+RIGHT*2.5,UP)
        polar_y_axis = rect_y_axis.copy().next_to(RIGHT*3.5+UP*2.5,RIGHT)

        polarPlaneGroup = Group(polarPlane,polar_x_axis,polar_y_axis)

        self.play(
            FadeIn(rectPlaneGroup),
            FadeIn(polarPlaneGroup),
            run_time = 2
        )
        self.wait()

        def expZTransform(z):
            z = np.exp(z) #lambda z: np.exp(z)-np.exp((z-z.conjugate())/2) Convierte el primer cuadrante en un circulo
            return z

        line_rect_1 = Line(rectPlane.coords_to_point(-1,-1),rectPlane.coords_to_point(0,1)).set_color(TEAL_C).set_z_index(1)
        line_rect_2 = Line(rectPlane.coords_to_point(0,1),rectPlane.coords_to_point(1,-1)).set_color(TEAL_C).set_z_index(1)
        line_rect_3 = Line(rectPlane.coords_to_point(1,-1),rectPlane.coords_to_point(-1,-1)).set_color(TEAL_C).set_z_index(1)
        dot_rect_1 = Dot(line_rect_1.get_start()).scale(0.8).set_color(YELLOW_D).set_z_index(2)
        dot_rect_2 = Dot(line_rect_2.get_start()).scale(0.8).set_color(GREEN).set_z_index(2)
        dot_rect_3 = Dot(line_rect_3.get_start()).scale(0.8).set_color(BLUE).set_z_index(2)
        dot_rect_1_lbl = MathTex('z_1').scale(0.8).set_opacity(0.7).next_to(dot_rect_1,LEFT).set_z_index(2)
        dot_rect_2_lbl = MathTex('z_2').scale(0.8).set_opacity(0.7).next_to(dot_rect_2,RIGHT).set_z_index(2)
        dot_rect_3_lbl = MathTex('z_3').scale(0.8).set_opacity(0.7).next_to(dot_rect_3,RIGHT).set_z_index(2)

        line_rect = Group(line_rect_1,line_rect_2,line_rect_3)
        dot_rect = Group(dot_rect_1,dot_rect_2,dot_rect_3)
        dot_rect_lbl = Group(dot_rect_1_lbl,dot_rect_2_lbl,dot_rect_3_lbl)

        line_polar_1 = Line([-1,-1,0],[0,1,0]).set_color(PURPLE_C).set_z_index(1)
        line_polar_1.apply_complex_function(expZTransform).shift(RIGHT*3.5)
        line_polar_2 = Line([0,1,0],[1,-1,0]).set_color(PURPLE_C).set_z_index(1)
        line_polar_2.apply_complex_function(expZTransform).shift(RIGHT*3.5)
        line_polar_3 = Line([1,-1,0],[-1,-1,0]).set_color(PURPLE_C).set_z_index(1)
        line_polar_3.apply_complex_function(expZTransform).shift(RIGHT*3.5)
        dot_polar_1 = Dot(line_polar_1.get_start()).scale(0.8).set_color(YELLOW_D).set_z_index(2)
        dot_polar_2 = Dot(line_polar_2.get_start()).scale(0.8).set_color(GREEN).set_z_index(2)
        dot_polar_3 = Dot(line_polar_3.get_start()).scale(0.8).set_color(BLUE).set_z_index(2)
        dot_polar_1_lbl = MathTex('w_1').scale(0.8).set_opacity(0.7).next_to(dot_polar_1,RIGHT).set_z_index(2)
        dot_polar_2_lbl = MathTex('w_2').scale(0.8).set_opacity(0.7).next_to(dot_polar_2,RIGHT).set_z_index(2)
        dot_polar_3_lbl = MathTex('w_3').scale(0.8).set_opacity(0.7).next_to(dot_polar_3,RIGHT).set_z_index(2)

        line_polar = Group(line_polar_1,line_polar_2,line_polar_3)
        dot_polar = Group(dot_polar_1,dot_polar_2,dot_polar_3)
        dot_polar_lbl = Group(dot_polar_1_lbl,dot_polar_2_lbl,dot_polar_3_lbl)

        self.play(
            FadeIn(dot_rect_1),
            FadeIn(dot_rect_1_lbl),
            FadeIn(dot_polar_1),
            FadeIn(dot_polar_1_lbl)
        )

        self.wait()
        self.play(
            Create(line_rect_1),
            Create(line_polar_1),
            run_time = 2
        )

        self.play(
            FadeIn(dot_rect_2),
            FadeIn(dot_rect_2_lbl),
            FadeIn(dot_polar_2),
            FadeIn(dot_polar_2_lbl)
        )

        self.wait()
        self.play(
            Create(line_rect_2),
            Create(line_polar_2),
            run_time = 2
        )

        self.play(
            FadeIn(dot_rect_3),
            FadeIn(dot_rect_3_lbl),
            FadeIn(dot_polar_3),
            FadeIn(dot_polar_3_lbl)
        )

        self.wait()
        self.play(
            Create(line_rect_3),
            Create(line_polar_3),
            run_time = 2
        )

        self.wait(2)

        self.play(
            FadeOut(line_polar),
            FadeOut(dot_polar),
            FadeOut(dot_polar_lbl),
            FadeOut(line_rect),
            FadeOut(dot_rect),
            FadeOut(dot_rect_lbl),
            FadeOut(polarPlaneGroup),
            FadeOut(rectPlaneGroup),
            FadeOut(eq_group)
        )
        self.wait()

class ExpZ_6(Scene):
    def construct(self):
        ##------------------------------
        ## Logo LME en la esquina
        ##------------------------------
        brand = Text(
            "LED Me Explain",
            fill_opacity = 0.5,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_color,"[3:4]":LME_color,"[5:6]":LME_color} ## Los espacios no cuentan como caracteres
        ).scale(0.4).to_edge(DR)
        # Añade el logo
        self.add(brand)
        ##---------------------------------
        ##---------------------------------

        text_1 = Tex( # Crea el título
            r"¿Y cómo se vería la transformación ", r'$z$',r'$\,\rightarrow\,$',r'${1 \over z}$',r' ?',
        ).scale_to_fit_width(config["frame_width"]-4)
        text_1_math = MathTex(r'z',r'\,\rightarrow',r'{1 \over z}', tex_template = TexFontTemplates.libertine).move_to(text_1[2]).shift(RIGHT*.1)
        text_1_math[0].set_color(TEAL_C)
        text_1_math[2].set_color(PURPLE_C)
        text_1_sub = Tex(r'Eso será tema para otro video').scale(0.8).next_to(text_1,DOWN, aligned_edge = RIGHT).shift(DOWN*.2)

        self.play(
            FadeIn(text_1[0]),
            FadeIn(text_1[4]),
            FadeIn(text_1_math)
        )
        self.wait()
        self.play(
            Write(text_1_sub)
        )
        self.wait()

        self.play(
            FadeOut(text_1[0]),
            FadeOut(text_1[4]),
            FadeOut(text_1_math),
            FadeOut(text_1_sub)
        )

        self.wait()
