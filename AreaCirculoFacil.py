from manim import *

config['frame_rate'] = 1 

class ACF_1(Scene):
    def construct(self):
        ##------------------------------
        ## Funciones
        ##------------------------------
        def dividedCircle(pieces = 2, radius = 1,  color1 = RED, color2 = GREEN, color3 = PURPLE, color4 = GOLD, shift = ORIGIN):
            group01 = VGroup()
            group02 = VGroup()
            group1 = VGroup()
            group2 = VGroup()

            for i in list(range(pieces)) :
                annularSec = AnnularSector(inner_radius = 0,outer_radius = radius, angle = TAU/pieces,start_angle = TAU/pieces*i).shift(shift)
                if i < pieces/2 :
                    if i%2 == 0 :
                        annularSec.set_color(color2)
                    else:
                        annularSec.set_color(color1)
                    group1.add(annularSec.copy())
                    group01.add(annularSec)
                else:
                    if i%2 == 0 :
                        annularSec.set_color(color4)
                    else:
                        annularSec.set_color(color3)
                    group2.add(annularSec.copy())
                    group02.add(annularSec)
            return [group01,group02,group1,group2]

        def rotatePieces(group, up = True,origin = ORIGIN):
            aux_divs = len(group)*2

            if up :
                flag = 1
            else :
                flag = -1

            for i in list(range(len(group))) :
                group[i].rotate(PI/2-TAU/aux_divs/2-TAU/aux_divs*i,about_point=origin)

            group.arrange(LEFT*flag,buff=0)

            return group
        ##---------------------------------
        ##---------------------------------

        ##------------------------------
        ## Logo LME en la esquina
        ##------------------------------
        brand = Text(
            "LED Me Explain",
            fill_opacity = 0.5,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).to_edge(DR)
        # Añade el logo
        self.add(brand)
        ##---------------------------------
        ##---------------------------------

        ##------------------------------
        ## Titulo y subtitulo del video
        ##------------------------------
        title = Text( # Crea el título
            "¿Cómo demostrar el área del círculo?",
            color = WHITE
        ).scale_to_fit_width(config["frame_width"]-4)

        # Crea el rectangulo que rodea al grupo
        frameTitle = SurroundingRectangle(title, buff = 1).set_color_by_gradient([LME_A,RED,LME_C])

        subtitle = Text( # Crea el subtítulo
            "Parte 1. Geometría",
            color = LIGHT_GREY
        ).scale(0.6).next_to(frameTitle,DOWN, aligned_edge = RIGHT)


        # Aparece el titulo
        self.play(Write(title) , run_time = 0.8)
        # Crea el rectangulo
        self.play(Create(frameTitle))
        # Escribe el subtitulo
        self.play(Write(subtitle),run_time = 0.7)
        self.wait(1.5) # Espera un momento
        # Desaparece el titulo, subtitulo y el rectangulo
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(frameTitle),
            run_time = 0.8
        )
        ##---------------------------------
        ##---------------------------------

        # Circulo maestro !!NO BORRAR NI MOVER DE LUGAR!!
        circle = Circle(radius = 1.5).set_color(WHITE)
        circle_center = circle.get_center()

        divs = [int(2**(i+2)) for i in list(range(6))]

        divided01 = []
        divided02 = []
        divided1 = []
        divided2 = []

        for i in divs :
            aux = dividedCircle(i,radius = circle.radius,shift = circle_center)
            divided01.append(aux[0])
            divided02.append(aux[1])
            divided1.append(aux[2])
            divided2.append(aux[3])

        for i in list(range(len(divided01))):
            divided1[i] = rotatePieces(divided1[i],up = True,origin = circle_center)
            divided1[i].move_to(circle_center+UP*circle.radius,aligned_edge = UP)
            divided2[i] = rotatePieces(divided2[i],up = False,origin = circle_center)
            divided2[i].move_to(circle_center+DOWN*circle.radius, aligned_edge = DOWN)


        aux_div1 = divided01[0].copy()
        aux_div2 = divided02[0].copy()

        self.wait()

        self.play(Create(circle))

        line_D_aux0 = Line(circle_center+LEFT*circle.radius,circle_center+RIGHT*circle.radius).set_color(ORANGE).set_stroke(width=6).set_z_index(2)
        lbl_D0 = MathTex(r'D', tex_template = TexFontTemplates.libertine).set_color(ORANGE).scale(1.3).next_to(line_D_aux0,RIGHT).set_z_index(2)

        self.wait()

        self.play(
            Create(line_D_aux0),
            FadeIn(lbl_D0),
            run_time = 0.7
        )

        self.wait()


        circle_per = circle.copy().set_color(TEAL)
        lbl_piD0 = MathTex(r'\pi D', tex_template = TexFontTemplates.libertine).scale(1.3).next_to(circle,DOWN).set_color(TEAL)

        self.play(
            Create(circle_per),
            FadeIn(lbl_piD0),
            run_time = 0.7)

        self.wait()

        line_r_aux0 = Line(circle_center,circle_center+RIGHT*circle.radius).set_color(YELLOW).set_stroke(width=6).set_z_index(2)
        lbl_r0 = MathTex(r'r', tex_template = TexFontTemplates.libertine).set_color(YELLOW).scale(1.3).next_to(line_r_aux0,RIGHT)

        self.play(
            line_D_aux0.animate.become(line_r_aux0),
            lbl_D0.animate.become(lbl_r0),
            run_time = 0.7
        )
        self.wait()

        lbl_2pir0 = MathTex(r'2 \pi r', tex_template = TexFontTemplates.libertine).scale(1.3).next_to(circle,DOWN).set_color(PURPLE)

        self.play(
            circle_per.animate.set_color(PURPLE),
            TransformMatchingShapes(lbl_piD0,lbl_2pir0),
            run_time = 0.7
        )

        self.wait()

        self.play(
            Uncreate(circle_per),
            FadeOut(lbl_2pir0),
            run_time = 0.7
        )

        self.wait()

        line_pir_aux0 = Arc(radius = circle.radius,start_angle = PI, angle = PI, arc_center = circle_center).set_stroke(width=6).set_color(PURE_GREEN).set_z_index(10)
        lbl_pir0 = MathTex(r'\pi r', tex_template = TexFontTemplates.libertine).set_color(PURE_GREEN).scale(1.3).next_to(line_pir_aux0,DOWN).set_z_index(10)

        self.play(
            Create(line_pir_aux0),
            FadeIn(lbl_pir0),
            run_time = 0.7
        )


        self.wait()

        self.play(FadeIn(Group(aux_div1,aux_div2)), lag_ratio=0.5, run_time = 3)

        self.wait()

        self.play(
            FadeOut(circle),
            Uncreate(line_D_aux0),
            FadeOut(lbl_D0),
            Uncreate(line_pir_aux0),
            FadeOut(lbl_pir0),
            run_time = 0.7
        )

        self.wait()

        exclude_animations = [1,3,4,6]

        for i in list(range(len(divided01))):
            if i != 0:
                # Hacer más divisiones
                self.play(
                    aux_div1.animate.become(divided01[i]),
                    aux_div2.animate.become(divided02[i]),
                    run_time = 0.7
                )
                self.wait()

            if not i in exclude_animations :
                # Desdoblar las piezas
                self.play(aux_div1.animate.become(divided1[i]))
                self.wait()
                self.play(aux_div2.animate.become(divided2[i]))
                self.wait()

                # Empalmar la parte de arriba con la de abajo
                aux_mov = RIGHT*circle.radius*np.cos(3*PI/2+TAU/divs[i]/2)+UP*circle.radius*np.sin(3*PI/2+TAU/divs[i]/2)
                self.play(aux_div1.animate.shift(aux_mov))
                self.wait()

                # Crear linea de radio con etiqueta
                line_r_aux = Line(aux_div1[0].get_bottom(),aux_div1[0].get_bottom()+RIGHT*circle.radius*np.cos(PI/2-TAU/divs[i]/2)+UP*circle.radius*np.sin(PI/2-TAU/divs[i]/2)).set_color(YELLOW).set_stroke(width=6)
                lbl_r = MathTex(r'r', tex_template = TexFontTemplates.libertine).set_color(YELLOW).scale(1.3).next_to(line_r_aux,RIGHT)

                # Crear longitud de los arcos con etiqueta
                line_pir_aux = Arc(radius = circle.radius,start_angle = 3*PI/2-TAU/divs[i]/2, angle = TAU/divs[i],arc_center = aux_div2[0].get_top()).set_stroke(width=6)
                for j in list(range(len(aux_div2))):
                    if j != 0:
                        line_pir_aux.append_points(Arc(radius = circle.radius,start_angle = 3*PI/2-TAU/divs[i]/2, angle = TAU/divs[i],arc_center = aux_div2[j].get_top()).get_points())

                line_pir_aux.set_color(PURE_GREEN)
                lbl_pir = MathTex(r'\pi r', tex_template = TexFontTemplates.libertine).set_color(PURE_GREEN).scale(1.3).next_to(line_pir_aux,DOWN)

                # Mostrar radio y longitud de arco
                self.play(
                    Create(line_r_aux),
                    FadeIn(lbl_r),
                    run_time = 0.7
                )

                self.wait()

                self.play(
                    Create(line_pir_aux),
                    FadeIn(lbl_pir),
                    run_time = 0.7
                )
                self.wait()

                if i < len(divided01)-1:
                    self.play(
                        Uncreate(line_r_aux),
                        FadeOut(lbl_r),
                        Uncreate(line_pir_aux),
                        FadeOut(lbl_pir),
                        run_time = 0.7
                    )
                    self.wait()
                    # Desempalmar las piezas
                    self.play(aux_div1.animate.shift(aux_mov*-1))
                    self.wait()

                    # Regresar a circulo las piezas
                    self.play(aux_div2.animate.become(divided02[i]))
                    self.wait()
                    self.play(aux_div1.animate.become(divided01[i]))

                    self.wait()

        rect = Group(aux_div1,aux_div2,line_r_aux,lbl_r,line_pir_aux,lbl_pir)
        line_r_aux0 = Line(circle_center,circle_center+RIGHT*circle.radius).set_color(YELLOW).set_stroke(width=6)
        line_pir_aux0 = Arc(radius = circle.radius,start_angle = PI, angle = PI, arc_center = circle_center).set_stroke(width=6).set_color(PURE_GREEN)
        circ = Group(divided01[-1],divided02[-1],line_r_aux0,lbl_r0,line_pir_aux0,lbl_pir0).move_to(UP+LEFT*4)

        self.play(
            rect.animate.move_to(UP+RIGHT*3),
            FadeIn(circ, target_position = ORIGIN)
        )

        area_circ = Circle(radius=circle.radius,color=TEAL,fill_opacity=0.7).move_to(divided01[-1].get_bottom())
        area_rect = Rectangle(color = TEAL,fill_opacity=0.7,height=circle.radius,width=PI*circle.radius).move_to(aux_div1.get_center())

        self.wait()

        self.play(FadeIn(area_circ))

        self.wait()

        self.play(area_circ.animate.become(area_rect))

        self.wait()

        eq_2 = MathTex(r'A',r'=',r'\pi',r'r^',r'2', tex_template = TexFontTemplates.libertine).scale(2).shift(DOWN*1.5)
        eq_2[0].set_color(TEAL)
        eq_1 = MathTex(r'A',r'=',r'\pi r\,',r'\,r', tex_template = TexFontTemplates.libertine).scale(2).move_to(eq_2,aligned_edge = DOWN)
        eq_1[0].set_color(TEAL)
        eq_1[2].set_color(PURE_GREEN)
        eq_1[3].set_color(YELLOW)
        eq_0 = MathTex(r'A',r'=',r'\,\,b\,',r'\,h', tex_template = TexFontTemplates.libertine).scale(2).move_to(eq_2,aligned_edge = DOWN)
        eq_0[0].set_color(TEAL)

        self.play(Transform(area_circ,eq_0[0].copy().set_color(TEAL)))

        self.wait()

        self.play(Write(eq_0))

        self.remove(area_circ)
        self.wait()

        self.play(
            FadeOut(eq_0[2],shift=DOWN),
            FadeIn(eq_1[2],target_position = lbl_pir)
        )

        self.play(
            FadeOut(eq_0[3],shift=DOWN),
            FadeIn(eq_1[3],target_position = lbl_r)
        )
        self.play(TransformMatchingShapes(eq_0[0:2],eq_1[0:2]))

        self.wait()


        self.play(
            TransformMatchingShapes(eq_1[2],eq_2[2]),
            TransformMatchingShapes(eq_1[3],eq_2[3]),
            FadeIn(eq_2[4])
        )
        self.play(eq_1[0:2].animate.move_to(eq_2[0:2]))

        self.add(eq_2[0])
        self.add(eq_2[1])
        self.remove(eq_1[0])
        self.remove(eq_1[1])

        self.wait()

        self.play(
            FadeOut(rect),
            FadeOut(circ),
            run_time = 0.7
        )

        self.wait()

        circle.shift(UP*1.5).set_fill(color=TEAL,opacity=0.7)
        self.play(DrawBorderThenFill(circle))

        line_r_aux0 = Line(circle.get_center(),circle.get_center()+RIGHT*circle.radius).set_color(YELLOW).set_stroke(width=6).set_z_index(2)
        lbl_r0 = MathTex(r'r', tex_template = TexFontTemplates.libertine).set_color(YELLOW).scale(1.3).next_to(line_r_aux0,RIGHT)

        self.play(
            Create(line_r_aux0),
            FadeIn(lbl_r0),
            eq_2[3].animate.set_color(YELLOW)
        )

        self.play(Circumscribe(eq_2,color=TEAL,buff=0.3))

        self.wait()

        self.play(
            FadeOut(circle),
            FadeOut(line_r_aux0),
            FadeOut(lbl_r0),
            FadeOut(eq_2),
            run_time = 1.5
        )

        self.wait()
