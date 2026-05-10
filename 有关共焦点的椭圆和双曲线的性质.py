from manim import *

config.tex_template = TexTemplateLibrary.ctex

def transform(obj:Mobject) -> Mobject: 
    return obj.scale(.6).shift(RIGHT*3.7)

class ConfocalEllipseHyperbola(Scene):
    def construct(self):
        Text.set_default(font_size=20, font="SimSong")
        MathTex.set_default(font_size=27)

        self.introduce()
        self.draw()
        self.properties()
        self.conclusion()

    def introduce(self):
        title = Text(
            "有关共焦点的椭圆和双曲线的性质", font="STHeiti", weight=BOLD, color=YELLOW
        ).scale(1.5)
        self.title = title
        self.play(Write(title),run_time=1)
        self.wait(2)
        self.play(title.animate.to_edge(UP, 1))
        self.wait(1)

    def draw(self):
        # 创建坐标系，放在屏幕右边1/2处，并缩小图形
        axes = (
            transform(Axes(
                x_range=[-1.5, 1.5, 1],
                y_range=[-2.5, 2.5, 1],
                axis_config={"color": WHITE, "include_ticks": False},
                x_length=8,
                y_length=8,
            ))
        )

        # 绘制椭圆：x^2/9 + y^2/4 = 1 (a=3, b=2)
        ellipse = transform(ImplicitFunction(
            lambda x, y: (x**2)/9 + (y**2)/4 - 1,
            color=BLUE,
            stroke_width=3,
            x_range=[-5, 5],
            y_range=[-4, 4],
        ))

        # 绘制双曲线：x^2/2 - y^2/3 = 1 (m=sqrt(2), n=sqrt(3))
        
        hyperbola = transform( ImplicitFunction(
            lambda x, y: (x**2)/1 - (y**2)/4 - 1,
            color=RED,
            stroke_width=3,
            x_range=[-5, 5],
            y_range=[-4, 4],
        )) 

        fs = transform(VGroup(
            Dot([2.23607,0,0]),
            Dot([-2.23607,0,0]),
        ))
        f_labels  = (VGroup(
            MathTex("F_2").move_to(fs[0].get_center() + [0,-.25,0]),
            MathTex("F_1").move_to(fs[1].get_center() + [0,-.25,0])
        ))
        
        dotA = transform(Dot([1.96371,3.38004,0]))
        dotB = transform(Dot([.24095,1.99354,0]))
        dotC = transform(Dot([2.12216,1.41365,0]))
        l_AF1 = Line(dotA.get_center(),fs[1].get_center())
        l_AF2 = Line(dotA.get_center(),fs[0].get_center())
        

        # 标题下方说明
        # explanation =.next_to(self.title, DOWN, .2, ORIGIN).to_edge(LEFT, .4)

        explanation = VGroup(
            Tex(  
                r"椭圆 $\dfrac{x^2}{a^2 }+ \dfrac{y^2}{ b^2} = 1$ 和双曲线$\dfrac{ x^2}{ m^2} - \dfrac{y^2}{ n^2 }= 1$ 共焦点$F_1, F_2$"
            ),
            Tex(
                r"点$A$为椭圆外双曲线上一点，线段$AF_1,AF_2$交椭圆于点$B,C$"
            ),
            Tex(r'则线段$BF_2,CF_1$的焦点$D$在双曲线上')

        ).arrange(DOWN, .2, aligned_edge= LEFT) \
        .next_to(self.title, DOWN, .2, ORIGIN).to_edge(LEFT, .4)
    

        # 添加到场景
        self.play(Write(explanation[0]))
        self.play(Create(axes), Create(ellipse), Create(hyperbola), Create(fs), Write(f_labels))
        self.wait(2)

        self.play(Write(explanation[1]))
        self.play(Create(dotA))
        # self.play(FadeIn(l_AF1))
        self.play(Create(dotB))

    def properties(self):
        pass

    def conclusion(self):
        self.wait(2)


if __name__ == '__main__' :
    with tempconfig({
        'quality': 'low_quality',
        # 'quality': 'high_quality',
        'preview': True,
        'write_to_movie': True,
        # "save_last_frame": True,
    }):
        # 实例化你的场景并开始渲染
        scene = ConfocalEllipseHyperbola()
        scene.render()