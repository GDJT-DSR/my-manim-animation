from manim import *

config.tex_template = TexTemplateLibrary.ctex


class CauchyEquation2(Scene):

    def construct(self):

        #设置字体字号
        Text.set_default(font_size=20,font="SimSong")
        MathTex.set_default(font_size=27)

        self.introduce()
        self.basic()

        self.condition3()
        self.wait(5)

        
    def introduce(self):

        self.tex1 = Tex('$f(x)+f(y)=f(x+y)$').scale(1.3).shift([0,.7,0])
        self.play(Create(self.tex1))
        self.wait(2)

        #显示题目
        title = Text('柯西方程',color=YELLOW,font='STHeiti',weight=BOLD)
        title.scale(1.6)
        # title.next_to(tex1,DOWN,.3,ORIGIN)
        self.play(Write(title))
        self.wait(4)

        self.play(self.tex1.animate.to_edge(UL,1),Uncreate(title))
        self.wait(2)
    def basic(self):
        self.prop = Tex('对任意','有理数','$q$和实数$x$，均有$f(qx)=qf(x)$').scale(1.08).next_to(self.tex1,DOWN,.4,LEFT).set_color(YELLOW)
        self.wait(1)
        self.play(Write(self.prop))
        self.wait(3)

    def condition3(self):
        # g = VGroup(g1)

        condition = Tex(r'(3)$f(x)$是单调函数')
        condition.next_to(self.prop,DOWN,.3,LEFT)
        self.play(Write(condition))
        self.wait(1)
        self.condition_text = condition

        g1 = VGroup()
        axes = Axes([-1.2,1.2],[-1.2,1.5],4,4)
        axes.to_edge(RIGHT,.6)
        self.play(Create(axes))
        g1.add(axes)

        d1 = Dot(axes.coords_to_point(1,1),.05)
        d1l = MathTex('(x,f(x))').next_to(d1,LEFT,.2)
        self.play(Create(d1),Write(d1l))
        self.wait(1)
        g1.add(d1,d1l)

        for i in range(-5,6):
            d = Dot(axes.coords_to_point(i/5,i/5),.05,color=WHITE,fill_opacity=.7)
            g1.add(d)
            self.play(Create(d),run_time=0.1)

        points = [axes.coords_to_point(x, y) for x, y in [(-0.2,-0.2),(-0.2,0.2),(0.2,0.2),(0.2,-0.2)]]
        
        # 创建正方形
        square = Polygon(*points, color=BLUE, fill_opacity=0.3, stroke_width=0)
        g1.add(square)
        self.play(Create(square))

        thought1 = VGroup(
            Tex('单调性$\\to$不等关系'),
            Tex('正方形$\\to$某个邻域'),
        ).arrange(RIGHT,.5,aligned_edge=ORIGIN).next_to(condition,DOWN,.3,LEFT)
        thought2 = Tex('$f(x)$在$x=0$处连续？').set_color(PINK).next_to(thought1,DOWN,.3,LEFT)

        self.play(Write(thought1))
        self.wait(1)
        self.play(Write(thought2))
        self.wait(2)
        self.play(FadeOut(VGroup(thought1,thought2)))
        self.wait(1)


        claim1 = Tex(r'Claim1:对$\forall x\in[0,c]$，均有$|f(x)|\le |f(c)|.$')
        claim1.next_to(condition,DOWN,.2,LEFT).set_color(GREEN)
        claim1_p = VGroup(
            Tex(r'若$f(x)$单调递增，则$0\le f(x)\le f(c)$'),
            Tex(r'若$f(x)$单调递减，则$0\ge f(x)\ge f(c)$'),
            Tex('均可得到题述条件成立'),
        ).arrange(DOWN,.2,aligned_edge=LEFT).next_to(claim1,DOWN,.2,LEFT)

        self.play(Write(claim1))
        self.wait(2)
        self.play(Write(claim1_p),run_time=3)
        self.wait(2)
        self.play(FadeOut(claim1_p))
        self.wait(1)

        goal  = Tex(r'要证：对任意的$\varepsilon>0$，存在$\delta$使得对任意$|x|<\delta$，均有$|f(x)|<\varepsilon$')
        goal.next_to(claim1,DOWN,.2,LEFT)
        self.play(Write(goal))

        prf = VGroup(
            Tex(r'$|f(x)|=|f(|x|)|\le |f(\delta)|$'),
            Tex(r'取$\delta=q\cdot|x_0|$($q\in\mathbb{Q}$)，则$|f(\delta)|=|q|\cdot|f(x_0)|$'),
            Tex(r'只需使$0<q<\dfrac{\varepsilon}{|f(x_0)|}$即可'),
            Tex(r'设正整数$N>\dfrac{|f(x_0)|}{\varepsilon}$，则$q=\dfrac1N$满足条件'),
            Tex('因此，存在满足条件的$\\delta$，则','$f(x)$在$x=0$处连续')
        ).arrange(DOWN,.2,aligned_edge=LEFT).next_to(goal,DOWN,.2,LEFT)

        self.play(Write(prf[0]))
        self.play(Indicate(self.prop),run_time=0.6)

        for i in range(1,5):
            self.play(Write(prf[i]))
            self.wait(1)

        self.wait(2)
        self.play(FadeOut(prf))
        self.wait(1)
        
        res2 = Tex('则$f(x)$在$0$处连续').next_to(goal,DOWN,.2,LEFT)
        self.play(Write(res2))
        self.wait(1)
        res3 = Tex('从而$f(x)$是连续函数').next_to(res2,DOWN,.2,LEFT)
        self.play(Write(res3))
        self.wait(1)

        res4 = Tex('进而利用连续条件可以得到$f(x)$的图像是一条直线').next_to(res3,DOWN,.2,LEFT)
        self.play(Write(res4))
        self.wait(5)
        
