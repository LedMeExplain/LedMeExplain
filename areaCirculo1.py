from manim import *

quality_factor = 1
fps = 30
dark_theme = True
config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

if dark_theme :
    TEXT_COLOR = WHITE
else:
    TEXT_COLOR = GRAY_E
    config['background_color'] = LME_E



class areaCirculo1(Scene):
    def construct(self):

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

        title = MathTex(r'\text{¿Por qué el área del círculo es}',r'\,\pi r^2\,',r'\text{?}', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_color(TEXT_COLOR)
        title[1].set_color(LME_B)
        rect_title = SurroundingRectangle(title,LME_B,buff = 0.4)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = TEXT_COLOR,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT)

        subtitle = Tex('Método 1').scale(0.55).set_opacity(0.8).next_to(rect_title,DOWN,aligned_edge = LEFT).set_color(TEXT_COLOR)

        self.add(title)
        self.play(Create(rect_title), run_time = 0.7)
        self.play(FadeIn(brand), run_time = 0.7)
        self.play(Write(subtitle),run_time = 0.7)

        # Circulo maestro !!NO BORRAR NI MOVER DE LUGAR!!
        circle = Circle(radius = 1.5,color = TEXT_COLOR).set_stroke(width = 6).shift(LEFT)
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

        self.play(FadeIn(Group(aux_div1,aux_div2)), lag_ratio=0.5, run_time = 3)
        self.wait(0.5)

        line_r_aux0 = Line(circle_center,circle_center+RIGHT*circle.radius).set_color(YELLOW).set_stroke(width=6)
        lbl_r0 = MathTex(r'r', tex_template = TexFontTemplates.libertine).set_color(YELLOW).scale(1.3).next_to(line_r_aux0,RIGHT)

        self.play(
            Create(line_r_aux0),
            FadeIn(lbl_r0),
            run_time = 0.7
        )
        self.wait(0.5)

        lbl_2pir0 = MathTex(r'2 \pi r', tex_template = TexFontTemplates.libertine).scale(1.3).next_to(circle,DOWN)

        self.play(Create(circle),FadeIn(lbl_2pir0), run_time = 0.7)
        self.wait(0.5)
        self.play(
            Uncreate(circle),
            FadeOut(lbl_2pir0),
            run_time = 0.7
        )

        self.wait(0.5)


        line_pir_aux0 = Arc(radius = circle.radius,start_angle = PI, angle = PI, arc_center = circle_center).set_stroke(width=6).set_color(PURE_GREEN)
        lbl_pir0 = MathTex(r'\pi r', tex_template = TexFontTemplates.libertine).set_color(PURE_GREEN).scale(1.3).next_to(line_pir_aux0,DOWN)

        self.play(
            Create(line_pir_aux0),
            FadeIn(lbl_pir0),
            run_time = 0.7
        )
        self.wait(0.5)
        self.play(
            Uncreate(line_r_aux0),
            FadeOut(lbl_r0),
            Uncreate(line_pir_aux0),
            FadeOut(lbl_pir0),
            run_time = 0.7
        )

        self.wait(0.3)

        exclude_animations = [1,3,4,6]

        for i in list(range(len(divided01))):
            if i != 0:
                # Hacer más divisiones
                self.play(
                    aux_div1.animate.become(divided01[i]),
                    aux_div2.animate.become(divided02[i])
                )
                self.wait(0.5)

            if not i in exclude_animations :
                # Desdoblar las piezas
                self.play(aux_div1.animate.become(divided1[i]))
                self.play(aux_div2.animate.become(divided2[i]))
                self.wait(0.5)

                # Empalmar la parte de arriba con la de abajo
                aux_mov = RIGHT*circle.radius*np.cos(3*PI/2+TAU/divs[i]/2)+UP*circle.radius*np.sin(3*PI/2+TAU/divs[i]/2)
                self.play(aux_div1.animate.shift(aux_mov))
                self.wait(0.5)

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
                    FadeIn(lbl_r)
                )
                self.wait(0.2)
                self.play(
                    Create(line_pir_aux),
                    FadeIn(lbl_pir),
                )
                self.wait(0.5)

                if i < len(divided01)-1:
                    self.play(
                        Uncreate(line_r_aux),
                        FadeOut(lbl_r),
                        Uncreate(line_pir_aux),
                        FadeOut(lbl_pir)
                    )
                    # Desempalmar las piezas
                    self.play(aux_div1.animate.shift(aux_mov*-1))

                    # Regresar a circulo las piezas
                    self.play(aux_div2.animate.become(divided02[i]))
                    self.play(aux_div1.animate.become(divided01[i]))
                    self.wait(0.5)

        rect = Group(aux_div1,aux_div2,line_r_aux,lbl_r,line_pir_aux,lbl_pir)
        line_r_aux0 = Line(circle_center,circle_center+RIGHT*circle.radius).set_color(YELLOW).set_stroke(width=6)
        line_pir_aux0 = Arc(radius = circle.radius,start_angle = PI, angle = PI, arc_center = circle_center).set_stroke(width=6).set_color(PURE_GREEN)
        circ = Group(divided01[-1],divided02[-1],line_r_aux0,lbl_r0,line_pir_aux0,lbl_pir0).shift(UP*3)
        self.play(rect.animate.shift(UP*.5))
        self.play(FadeIn(circ))
        self.wait(0.5)

        eq_0 = MathTex(r'A = ',r'b',r'\,\,\,\,h', tex_template = TexFontTemplates.libertine).scale(2).next_to(rect,DOWN,buff = .5)
        eq_1 = MathTex(r'A = ',r'\pi r ',r'\, r', tex_template = TexFontTemplates.libertine).scale(2).move_to(eq_0,aligned_edge = DL)
        eq_1[1].set_color(PURE_GREEN)
        eq_1[2].set_color(YELLOW)
        eq_2 = MathTex(r'A = ',r'\pi',r'r^2', tex_template = TexFontTemplates.libertine).scale(2).move_to(eq_0,aligned_edge = DL)

        self.play(FadeIn(eq_0))
        self.play(
            FadeIn(eq_1[1], target_position = lbl_pir),
            FadeOut(eq_0[1], shift = DOWN)
        )
        self.play(
            FadeIn(eq_1[2], target_position = lbl_r),
            FadeOut(eq_0[2], shift = DOWN)
        )
        self.wait()
        self.play(
            TransformMatchingShapes(eq_1[0],eq_2[0]),
            TransformMatchingShapes(eq_1[1],eq_2[1]),
            TransformMatchingShapes(eq_1[2],eq_2[2]),
        )
        self.wait(0.5)
        self.play(Circumscribe(eq_2,color = LME_A,buff = 0.25))
        self.wait()
