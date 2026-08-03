from manim import *

config.tex_template = TexTemplateLibrary.ctex

class MyScene(MovingCameraScene):
    def construct(self):
        #设置字体字号
        Text.set_default(font_size=29,font="SimSong")
        MathTex.set_default(font_size=29)

        self.introduce()
        self.solve()

    def introduce(self):
        center = ORIGIN
        a = 2.5
        b = 1.5
        c = np.sqrt(a**2-b**2)

        base_axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-1, 1, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True, "stroke_width": 2,"include_ticks": False},
        ).move_to(center)
        axes = always_redraw(lambda: base_axes.copy().move_to(center))
        ellipse = always_redraw(lambda: Ellipse(width=2 * a, height=2 * b).move_to(center))
        A0 = center + RIGHT * a
        A1 = A0 + LEFT * (a-c)
        A_pos = ValueTracker(0)

        def current_A():
            return A0 + (A1 - A0) * A_pos.get_value()

        point_A = always_redraw(lambda: Dot(current_A(), color=RED)).set_z_index(10)

        self.theta = ValueTracker(-PI / 2 + 0.3)

        def ellipse_intersections(line_angle):
            A = current_A()
            dx = np.cos(line_angle)
            dy = np.sin(line_angle)
            Ax, Ay = A[0], A[1]
            alpha = dx / a
            beta = dy / b
            gamma = Ax / a
            delta = Ay / b
            Aq = alpha ** 2 + beta ** 2
            Bq = 2 * (alpha * gamma + beta * delta)
            Cq = gamma ** 2 + delta ** 2 - 1
            disc = Bq ** 2 - 4 * Aq * Cq
            if disc < 0:
                return [A, A]
            sqrt_disc = np.sqrt(disc)
            t1 = (-Bq + sqrt_disc) / (2 * Aq)
            t2 = (-Bq - sqrt_disc) / (2 * Aq)
            p1 = A + np.array([dx, dy, 0]) * t1
            p2 = A + np.array([dx, dy, 0]) * t2
            return [p1, p2]

        def right_angle_marker():
            A = current_A()
            u = np.array([np.cos(self.theta.get_value()), np.sin(self.theta.get_value()), 0])
            v = np.array([np.cos(self.theta.get_value() + PI / 2), np.sin(self.theta.get_value() + PI / 2), 0])
            corner1 = A - u * 0.15
            corner2 = A - u * 0.15 - v * 0.15
            corner3 = A - v * 0.15
            marker = VMobject()
            marker.set_points_as_corners([corner1, corner2, corner3])
            marker.set_stroke(color=WHITE, width=3)
            return marker

        def line1_pts():
            p1, p2 = ellipse_intersections(self.theta.get_value())
            return p1, p2

        def line2_pts():
            p1, p2 = ellipse_intersections(self.theta.get_value() + PI / 2)
            return p1, p2

        def current_line1():
            p1, p2 = line1_pts()
            return Line(p1, p2, color=BLUE)

        def current_line2():
            p1, p2 = line2_pts()
            return Line(p1, p2, color=BLUE)

        def current_point_B():
            return Dot(line1_pts()[0], color=YELLOW, radius=0.08)

        def current_point_D():
            return Dot(line1_pts()[1], color=YELLOW, radius=0.08)

        def current_point_C():
            return Dot(line2_pts()[0], color=YELLOW, radius=0.08)

        def current_point_E():
            return Dot(line2_pts()[1], color=YELLOW, radius=0.08)

        def current_line_BC():
            return Line(line1_pts()[1], line2_pts()[1], color=GREEN)

        line1 = always_redraw(current_line1)
        line2 = always_redraw(current_line2)
        right_angle = always_redraw(right_angle_marker)

        point_B = always_redraw(current_point_B)
        point_D = always_redraw(current_point_D)
        point_C = always_redraw(current_point_C)
        point_E = always_redraw(current_point_E)

        line_BC = always_redraw(current_line_BC)

        self.play(Create(axes), Create(ellipse), FadeIn(point_A))
        self.play(Create(line1), Create(line2), Create(right_angle), Create(point_B), Create(point_C),Create(point_D), Create(point_E), Create(line_BC))

        self.play(self.theta.animate.set_value(-0.3), run_time=4)
        self.play(self.theta.animate.set_value(-PI / 2 + 0.3), run_time=4)
        self.wait(4)
        self.play(Uncreate(line_BC))
        self.play(A_pos.animate.set_value(1), run_time=4)

        def regression_line_for_current_points():
            def point_xy(point):
                coords = base_axes.point_to_coords(point)
                return np.array([float(coords[0]), float(coords[1])], dtype=float)

            point_coords = np.array([
                point_xy(line1_pts()[0]),
                point_xy(line2_pts()[0]),
                point_xy(line1_pts()[1]),
                point_xy(line2_pts()[1]),
            ], dtype=float)

            xs = point_coords[:, 0]
            ys = point_coords[:, 1]
            x_mean = np.mean(xs)
            y_mean = np.mean(ys)
            slope = np.sum((xs - x_mean) * (ys - y_mean)) / np.sum((xs - x_mean) ** 2)
            intercept = y_mean - slope * x_mean

            x_min, x_max = -2, 2
            y_min = slope * x_min + intercept
            y_max = slope * x_max + intercept

            p1 = base_axes.coords_to_point(x_min, y_min)
            p2 = base_axes.coords_to_point(x_max, y_max)
            return Line(p1, p2, color=ORANGE, stroke_width=3)

        regression_line = always_redraw(regression_line_for_current_points)

        self.play(Create(regression_line))
        self.play(self.theta.animate.set_value(PI / 3), run_time=4)
        self.play(self.theta.animate.set_value(- PI / 5), run_time=4)
        self.wait(4)

        self.play(
            self.camera.frame.animate.move_to([-3,-1.5,0]),
            run_time = 2
        )
        
        

    def solve(self):
        ec = MathTex(r"\text{设椭圆}  \frac{x^2}{a^2}+\frac{y^2}{b^2}=1")
        ec.move_to([-8, 1.5, 0])
        el = MathTex(r"\ell_1:\;y=k(x-c)  \ \ \ell_2:\;y=-\frac{1}{k}(x-c) ")
        el.next_to(ec, DOWN, .2, LEFT)

        lineeq1 = MathTex(r"y=\frac{\sum\limits_{i=1}^4x_iy_i-4\bar{x}\cdot\bar{y}}{\sum\limits_{i=1}^4x_i^2-4\bar{x}^2}(x-\bar{x})+\bar{y}")
        lineeq1.next_to(el, DOWN, .2, LEFT).set_color(YELLOW)
        
        self.play(Write(ec))
        self.wait(1.5)
        self.play(Write(el))
        self.wait(2)
        self.play(Write(lineeq1))
        self.wait(2)
        self.play(self.theta.animate.set_value(- PI / 2), run_time=1)
        self.wait(2)
        self.play(self.theta.animate.set_value(- PI / 5), run_time=1)

        lineeq2 = MathTex(r"0=\frac{\sum\limits_{i=1}^4x_iy_i-4\bar{x}\cdot\bar{y}}{\sum\limits_{i=1}^4x_i^2-4\bar{x}^2}(x_0-\bar{x})+\bar{y}")
        lineeq2.move_to(lineeq1,LEFT).set_color(YELLOW)
        self.play(ReplacementTransform(lineeq1, lineeq2))
        self.wait(1)

        # lineeq3 = MathTex(r"0=\frac{\sum\limits_{i=1}^4x_iy_i-4\bar{x}\cdot\bar{y}}{\sum\limits_{i=1}^4x_i^2-4\bar{x}^2}(x-\bar{x})+\bar{y}")
        lineeq3 = MathTex(r"x_0-\bar{x}=-\bar{y}\frac{\sum\limits_{i=1}^4x_i^2-4\bar{x}^2 }{ \sum\limits_{i=1}^4x_iy_i-4\bar{x}\cdot\bar{y}}")
        lineeq3.move_to(lineeq2,LEFT).set_color(YELLOW)
        self.play(ReplacementTransform(lineeq2, lineeq3))
        self.wait(1)

        lineeq4 = MathTex(r"x_0=\bar{x}-\bar{y}\frac{\sum\limits_{i=1}^4x_i^2-4\bar{x}^2 }{ \sum\limits_{i=1}^4x_iy_i-4\bar{x}\cdot\bar{y}}")
        lineeq4.move_to(lineeq3,LEFT).set_color(YELLOW)
        self.play(ReplacementTransform(lineeq3, lineeq4))
        self.wait(1)
        lineeq5 = MathTex(r"x_0=\frac{\bar{x}\sum\limits_{i=1}^4x_iy_i - \bar{y} \sum\limits_{i=1}^4x^2 }{ \sum\limits_{i=1}^4x_iy_i-4\bar{x}\cdot\bar{y}}")
        lineeq5.move_to(lineeq3,LEFT).set_color(YELLOW)
        self.play(ReplacementTransform(lineeq4, lineeq5))
        self.wait(1)
        lineeq6 = MathTex(r"x_0=\frac{\sum\limits_{i=1}^4x_i\sum\limits_{i=1}^4x_iy_i -\sum\limits_{i=1}^4y_i \sum\limits_{i=1}^4x_i^2 }{ 4 \sum\limits_{i=1}^4x_iy_i-\sum\limits_{i=1}^4x_i\sum\limits_{i=1}^4y_i}")
        lineeq6.move_to(lineeq3,LEFT).set_color(YELLOW)
        self.play(ReplacementTransform(lineeq5, lineeq6))
        self.wait(1)
        label = MathTex('=\\mathrm{constant}?')
        label.next_to(lineeq6, RIGHT, .2, ORIGIN)
        self.play(Write(label))
        self.wait(3)
        
        # 带入数值
        sx = VGroup(
            MathTex("x_1+x_2 = \\frac{2 a^{2} k^{2} c}{a^{2} k^{2} + b^{2}},\; x_3+x_4 =\\frac{2 a^{2} c}{a^{2} + b^{2} k^{2}}"),
            MathTex("\sum_{i=1}^4x_i= \\frac{2 a^{2} c \\left(2 a^{2} k^{2} + b^{2} k^{4} + b^{2}\\right)}{\\left(a^{2} + b^{2} k^{2}\\right) \\left(a^{2} k^{2} + b^{2}\\right)}"),
        ).arrange(DOWN, buff=.2, aligned_edge = LEFT).next_to(lineeq6, DOWN, .4, LEFT).set_color(PINK)
        self.play(Write(sx))
        self.wait(2)
        self.play(Unwrite(sx))

        sy = VGroup(
            MathTex('y_1+y_2 = - \\frac{2 b^{2} k c}{a^{2} k^{2} + b^{2}},\; y_3+y_4 = \\frac{2 b^{2} k t}{a^{2} + b^{2} k^{2}}'),
            MathTex('\sum_{i=1}^4y_i= \\frac{2 b^{2} c^3 k \\left(k^2-1\\right)}{\\left(a^{2} + b^{2} k^{2}\\right) \\left(a^{2} k^{2} + b^{2}\\right)}')
        ).arrange(DOWN, buff=.2, aligned_edge = LEFT).next_to(lineeq6, DOWN, .4, LEFT).set_color(GREEN)
        self.play(Write(sy))
        self.wait(2)
        self.play(Unwrite(sy))

        sxsq = VGroup(
            MathTex('x_1^2+x_2^2 =\\frac{2 a^{2} \\left(a^{4} k^{4} - a^{2} b^{2} k^{4} + b^{4} k^{2} + b^{4}\\right)}{\\left(a^{2} k^{2} + b^{2}\\right)^{2}},\; x_3^2+x_4^2 = \\frac{2 a^{2} \\left(a^{4} - a^{2} b^{2} + b^{4} k^{4} + b^{4} k^{2}\\right)}{\\left(a^{2} + b^{2} k^{2}\\right)^{2}}'),
            MathTex('\sum_{i=1}^4x_i^2= \\frac{2 a^{2} A}{\\left(a^{2} + b^{2} k^{2}\\right)^{2} \\left(a^{2} k^{2} + b^{2}\\right)^{2}}'),
            MathTex('\\text{其中}A=2 a^{8} k^{4} + 2 a^{6} b^{2} k^{6} - 2 a^{6} b^{2} k^{4} + 2 a^{6} b^{2} k^{2} + 2 a^{4} b^{4} k^{8} - a^{4} b^{4} k^{6} - a^{4} b^{4} k^{2} + 2 a^{4} b^{4}\\\\  - a^{2} b^{6} k^{8} +2 a^{2} b^{6} k^{6} + 4 a^{2} b^{6} k^{4} + 2 a^{2} b^{6} k^{2} - a^{2} b^{6} + b^{8} k^{6} + 2 b^{8} k^{4} + b^{8} k^{2}')
        ).arrange(DOWN, buff=.2, aligned_edge = LEFT).next_to(lineeq6, DOWN, .4, LEFT).set_color(PURPLE_B)
        self.play(Write(sxsq))
        self.wait(5)
        self.play(Unwrite(sxsq))

        sxy = VGroup(
            MathTex('x_1y_1+x_2y_2 = - \\frac{2 a^{2} b^{2} k \\left(- a^{2} k^{2} - b^{2} + 2 k^{2} t^{2}\\right)}{\\left(a^{2} k^{2} + b^{2}\\right)^{2}},\; x_3y_3+x_3y_4 = \\frac{2 a^{2} b^{2} k \\left(- a^{2} - b^{2} k^{2} + 2 t^{2}\\right)}{\\left(a^{2} + b^{2} k^{2}\\right)^{2}}'),
            MathTex('\sum_{i=1}^4x_iy_i= \\frac{2 a^{2} b^{2}c^2 k \\left(k^2-1\\right)B}{\\left(a^{2} + b^{2} k^{2}\\right)^{2} \\left(a^{2} k^{2} + b^{2}\\right)^{2}}'),
            MathTex('\\text{其中}B=a^{4} k^{2} - a^{2} b^{2} k^{4} - 4 a^{2} b^{2} k^{2} - a^{2} b^{2} - 2 b^{4} k^{4} - 3 b^{4} k^{2} - 2 b^{4}')
        ).arrange(DOWN, buff=.2, aligned_edge = LEFT).next_to(lineeq6, DOWN, .4, LEFT).set_color(BLUE)
        self.play(Write(sxy))
        self.wait(2)
        self.play(Unwrite(sxy))

        uptitle = Tex('分子=').next_to(lineeq6, DOWN, .5, LEFT).set_color(RED)
        up1 = VGroup(
            MathTex(r'\sum\limits_{i=1}^4x_i\sum\limits_{i=1}^4x_iy_i -\sum\limits_{i=1}^4y_i \sum\limits_{i=1}^4x_i^2'),
            MathTex('\\frac{4 a^{2} b^{2} c^{3}  \\left(k^{2} - 1\\right)}{\\left(a^2k^2+b^2\\right)^3\\left(a^2+b^2k^2\\right)^3}','\\left(a^{2} \\left(2 a^{2} k^{2} + b^{2} k^{4} + b^{2}\\right) \\cdot B -A\\right)'),
            MathTex('\\frac{4 a^{2} b^{2} c^{3}  \\left(k^{2} - 1\\right)}{\\left(a^2k^2+b^2\\right)^3\\left(a^2+b^2k^2\\right)^3}','\\left(- b^{2} \\left(a^{2} + b^{2} k^{2}\\right) \\left(3 a^{2} + b^{2}\\right) \\left(k^{2} + 1\\right)^{2} \\left(a^{2} k^{2} + b^{2}\\right)\\right)'),
            MathTex('-\\frac{4 a^{2} b^{4} c^{3}  \\left(k^{2} - 1\\right)\\left(3 a^{2} + b^{2}\\right) \\left(k^{2} + 1\\right)^{2}}{\\left(a^2k^2+b^2\\right)^2\\left(a^2+b^2k^2\\right)^2}  '),

        ).arrange(ORIGIN, aligned_edge = LEFT).next_to(uptitle, RIGHT, .1, ORIGIN).set_color(RED)
        self.play(Write(VGroup(uptitle,up1[0])))
        self.wait(1)
        for i in range(1,len(up1)):
            self.play(ReplacementTransform(up1[i-1], up1[i]))
            self.wait(2)

        downtitle = Tex('分母=').next_to(uptitle, DOWN, .8, LEFT).set_color(RED)
        down1 = VGroup(
            MathTex(r'4 \sum\limits_{i=1}^4x_iy_i-\sum\limits_{i=1}^4x_i\sum\limits_{i=1}^4y_i}'),
            MathTex('\\frac{4a^2b^2c^2k\\left(k^2-1\\right)}{\\left(a^2k^2+b^2\\right)^2\\left(a^2+b^2k^2\\right)^2}','\\left( 2B-c^2\\left( 2a^2k^2+b^2k^4+b^2 \\right) \\right)'),
            MathTex('\\frac{4a^2b^2c^2k\\left(k^2-1\\right)}{\\left(a^2k^2+b^2\\right)^2\\left(a^2+b^2k^2\\right)^2}','\\left(  -3b^2\\left(a^2+b^2\\right)\\left(k^2+1\\right)^2  \\right)'),
            MathTex('-\\frac{12a^2b^2c^2k\\left(k^2-1\\right)\\left(a^2+b^2\\right)\\left(k^2+1\\right)^2}{\\left(a^2k^2+b^2\\right)^2\\left(a^2+b^2k^2\\right)^2}'),
        ).arrange(ORIGIN, aligned_edge = LEFT).next_to(downtitle, RIGHT, .1, ORIGIN).set_color(RED)
        self.play(Write(VGroup(downtitle,down1[0])))
        self.wait(1)
        for i in range(1,len(down1)):
            self.play(ReplacementTransform(down1[i-1], down1[i]))
            self.wait(2)

        endvalue = MathTex(r'x_0 = \frac{c\left(3a^2+b^2\right)}{3\left(a^2+b^2\right)} = \mathrm{constant}')
        endvalue.next_to(downtitle, DOWN, .5, LEFT).set_color(YELLOW)
        self.play(Write(endvalue))
        self.wait(5)

    

# 生成视频并预览
with tempconfig({
    'quality': 'low_quality',
    # 'quality': 'high_quality',
    'preview': True,
    # 'save_last_frame' : True
    'write_to_movie': True,
    # "from_animation_number" : 
}):
    # 实例化你的场景并开始渲染
    scene = MyScene()
    scene.render()