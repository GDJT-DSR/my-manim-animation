from manim import *

config.tex_template = TexTemplateLibrary.ctex

class MyScene(Scene):
    def construct(self):
        #设置字体字号
        Text.set_default(font_size=29,font="SimSong")
        MathTex.set_default(font_size=29)

        self.introduce()
        self.solve()

    def introduce(self):
        self.title = VGroup(
            Tex(r'已知函数$f(x)$定义域为$\mathbf{R}$，且当$x<0$时，$f(x)=2^x$'),
            Tex(r'对$x_0\in\mathbf{R}$，定义$D(x_0)=\{ d\in\mathbf{R} \mid f(x_0+d)>f(x_0) \}$'),
            Tex(r'(3)\ 设$f(x)$满足:若$f(x_1)\le f(x_2)$，则$D(x_2)\subseteq D(x_1)$；'),
            Tex(r'$x\in(0,1)$时，$f(x)<f(0)$.\ 证明：'),
            Tex(r'(i) $f(0)\ge 1$\quad (ii) $f(x)$在$(0,+\infty)$上单调递增')

        ).arrange(DOWN,.3,aligned_edge=LEFT).scale(1.3).set_color(YELLOW)
        self.play(Create(self.title))
        self.wait(5)
        self.play(self.title.animate.scale(.8).to_edge(UP, .5).to_edge(LEFT, .6))

    def solve(self):

        box1 = SurroundingRectangle(self.title[2], buff=.1, color=BLUE)
        self.play(Create(box1))
        desc1 = VGroup(
            Tex(r'若$f(a)>f(b)\ge f(c)$'),
            Tex(r'则$D(b)\subseteq D(c)$'),
            Tex(r'即$a-b\in D(b)\Rightarrow a-b\in D(c)$'),
            Tex(r'则$f(a-b+c)>f(c)$')
        ).arrange(DOWN,.2,aligned_edge=LEFT).set_color(GREEN_B)
        desc1.to_edge(UP, 1).to_edge(RIGHT, .6)
        # self.play(Write(desc1))
        for i in desc1:
            self.play(Write(i))
            self.wait(1)
        self.wait(2)


        solutioni = VGroup(
            Tex(r'若$f(0)<1$，则存在$t\in(-1,0)$使得$f(t)>f(0)$'),
            Tex(r'则$f\left(\frac{t}{2}\right)>f(t)\ge f(0)$，则$f\left(-\frac{t}{2}\right)>f(0)$'),
            Tex(r'但由于$-\frac{t}{2}\in(0,1)$，矛盾')
        ).arrange(DOWN,.2,aligned_edge=LEFT).set_color(PURPLE_B).next_to(self.title,DOWN,.4,LEFT)
        for i in solutioni:
            self.play(Write(i))
            self.wait(1)
        self.wait(5)
        self.play(Unwrite(solutioni))

        self.wait(2)


        solutionii = VGroup(
            Tex(r'对$0<x_1<x_2$，只需证明$f(x_1)<f(x_2)$，',r'故只需证明'),
            Tex(r'由(i)知$f(x_1-x_2)<1\le f(0)$',r'，故只需$f(x_1)\le f(x_1-x_2)$'),
            Tex(r'假设$f(x_1)>f(x_1-x_2)$，',r'则对$m<x_1-x_2$，$f(x_1)>f(x_1-x_2)>f(m)$'),
            
            Tex(r'取$m$使得$m+x_2\in(0,1)$，','则有$f(0)>f(m+x_2)>f(m)$'),
            Tex(r'但$-x_2<m<0$，这与$f(x)$在$(-\infty,0)$上单调递增矛盾。')
        ).arrange(DOWN,.2,aligned_edge=LEFT)
        solutionii.next_to(self.title,DOWN,.4,LEFT).set_color(BLUE)
        
        self.play(Write(solutionii[0][0]))
        self.wait(2)
        self.play(Write(solutionii[0][1]))


        formula1 = VGroup(
            MathTex(r'f(k)>f(x_1-x_2+k)\ge f(x_1)'),
            MathTex(r'f(0)>f(x_1-x_2)\ge f(x_1)')
        ).set_color(PINK).next_to(solutionii[0],RIGHT,.2)
        self.play(Write(formula1[0]))
        self.wait(3)

        self.play(ReplacementTransform(formula1[0],formula1[1]))
        self.wait(3)

        self.play(Write(solutionii[1]))
        self.wait(3)
        for i in solutionii[2]:
            self.play(Write(i))
            self.wait(3)

        formula2 = MathTex('\\Rightarrow','f(m+x_2)','>f(m)').set_color(PINK).next_to(solutionii[2],RIGHT,.2)

        self.play(Write(formula2))
        self.wait(3)
        self.play(Write(solutionii[3]))

        formula3 = MathTex('\\Rightarrow f(-x_2)>f(m)').set_color(BLUE).next_to(solutionii[3],RIGHT,.2)
        self.play(Write(formula3))
        self.wait(3)
        self.play(Write(solutionii[4]))


# 生成视频并预览
with tempconfig({
    # 'quality': 'low_quality',
    'quality': 'high_quality',
    'preview': True,
    'write_to_movie': True
}):
    # 实例化你的场景并开始渲染
    scene = MyScene()
    scene.render()