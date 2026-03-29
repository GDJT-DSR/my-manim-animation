from manim import *

config.tex_template = TexTemplateLibrary.ctex

color_map = {
    "{x}":BLUE_A,
    "{y}":LIGHT_PINK,
    "{m}":GREEN_B,
    "{n}":PURPLE_A
}

class CauchyEquation(Scene):
    def construct(self):
        #设置字体字号
        Text.set_default(font_size=20,font="SimSong")
        MathTex.set_default(font_size=27)

        self.introduce()
        self.basic()
        self.wait(2)

        self.condition1()
        self.condition2()

        self.conclusion()

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
        
        prf1 = VGroup(
            Tex('令$y=0$，则有$f(x)+f(0)=f(x)$，则$f(0)=0$'),
            Tex('令$y=-x$，则有$f(x)+f(-x)=f(0)=0$即$f(x)$是奇函数')
        ).arrange(DOWN,.2,aligned_edge=LEFT).set_color(BLUE)
        prf1.next_to(self.tex1,DOWN,.3,LEFT)
        self.play(Write(prf1[0]))
        self.wait(1)
        self.play(Write(prf1[1]))
        self.wait(3)

        prop2 = VGroup(Tex('证明：对任意整数$n$和实数$x$，均有$f(nx)=nf(x)$')).set_color(GREEN_B)
        prop2.arrange(RIGHT,.1)
        prop2.next_to(prf1,DOWN,.3,LEFT)
        self.play(Write(prop2))
        self.wait(1)

        prf2 = VGroup(
            Tex('$n>0$时，对$n$归纳，$n=1$时显然成立，假设$n$时成立，考虑$n+1$时：'),
            Tex('$f[(n+1)x]=f(nx)+f(x)=nf(x)+f(x)=(n+1)f(x)$，结论成立'),
            VGroup(Tex('当$n=0$时，显然成立；'),Tex('当$n<0$，有$f(nx)=-f(-nx)=-(-n)f(x)=nf(x)$也成立')).arrange(RIGHT,.2)
            
        ).arrange(DOWN,.2,aligned_edge=LEFT).next_to(prop2,DOWN,.3,LEFT).set_color(GREEN_B)
        self.play(Write(prf2[0]))
        self.wait(1)
        self.play(Write(prf2[1]))
        self.wait(1)
        self.play(Write(prf2[2]))
        self.wait(3)
        # self.play(FadeOut(prf2))
        # self.wait(.5)

        prf3 = VGroup(
            Tex(r'对有理数$q=\dfrac nm(m,n\in\mathbb{Z})$，有$mf(qx)=f(qmx)=f(nx)=nf(x)$，'),
            Tex('那么$f(qx)=qf(x)$')
        ).arrange(RIGHT,0.2).next_to(prf2,DOWN,.2,LEFT).set_color(PURPLE_B)
        self.play(Write(prf3))

        prop3 = Tex('对任意','有理数','$q$和实数$x$，均有$f(qx)=qf(x)$').scale(1.2).next_to(prf3,DOWN,.4).set_color(YELLOW)
        self.wait(1)
        self.play(Write(prop3))
        self.wait(3)

        prop3c = prop3.copy()
        prop3c.scale(0.9).next_to(self.tex1,DOWN,.3,LEFT)

        self.play(FadeOut(prf1,prf2,prf3,prop2),Transform(prop3,prop3c),run_time=1.2)
        self.wait(1)

        box1 = SurroundingRectangle(prop3c[1])
        self.play(Create(box1))
        desc1 = MathTex(r'\mathbb{Q}\to \mathbb{R}\;?').next_to(box1,DOWN,.2,ORIGIN).scale(1.2).set_color(GREEN)
        times = MathTex(r'\times').scale(1.6).next_to(desc1,RIGHT,.4).set_color(RED)
        self.wait(1)
        self.play(Write(desc1))
        self.wait(2)
        self.play(Create(times))
        self.wait(2)
        # self.play(Uncreate(box1,times),Unwrite(desc1),run_time=1)
        self.wait(1)

        txt1 = Text('增加条件?',color=RED).scale(1.2)
        txt1.next_to(times,RIGHT,.4,ORIGIN)
        self.play(Write(txt1))
        self.wait(2)

        self.play(FadeOut(txt1,times,desc1,box1))
        self.tex2 = prop3c

    def condition1(self):
        g = VGroup()
        condition = Tex(r'(1)存在实数$c$，使得对任意实数$\lambda$均有$f(\lambda x)\le \lambda f(x)+c$')
        condition.next_to(self.tex2,DOWN,.3,LEFT)
        self.play(Write(condition))
        self.wait(1)
        g.add(condition)
        self.condition1_text = condition

        axes = Axes([-1.2,1.2],[-1.2,1.5],4,4)
        axes.to_edge(RIGHT,.6)
        self.play(Create(axes))
        g.add(axes)

        d1 = Dot(axes.coords_to_point(.5,.5),.05)
        d1l = MathTex('(x,f(x))').next_to(d1,RIGHT,.2)
        self.play(Create(d1),Write(d1l))
        self.wait(1)
        g.add(d1,d1l)

        for i in range(-10,11):
            d = Dot(axes.coords_to_point(i/10,i/10),.05,color=WHITE,fill_opacity=.5)
            g.add(d)
            self.play(Create(d),run_time=0.1)

        l1 = DashedLine(axes.coords_to_point(-1,-.5),axes.coords_to_point(1,1.5),color=YELLOW,stroke_width=3)
        self.play(Create(l1))
        self.wait(2)

        d2 = Dot(axes.coords_to_point(.42,.7),.05,color=PINK)
        self.play(Create(d2))
        self.wait(1)
        
        g.add(l1,d2)

        for i in range(21):
            t = (i-10)/5
            d = Dot(axes.coords_to_point(0.42*t,.7*t),.05,color=LIGHT_PINK)
            self.play(Create(d),run_time=0.1)
            g.add(d)
            if (i==20):
                self.wait(1)
                self.play(d.animate.set_color(RED))
                box = SurroundingRectangle(d)
                self.play(Create(box))
                self.wait(3)
                g.add(box)
        


        prf = VGroup(
            Tex(r'假设存在$\lambda_0$使得$f(\lambda_0 x)\neq \lambda_0 f(x)$，设$d=f(\lambda_0x)-\lambda_0f(x)$，'),
            Tex(r'则对任意整数$n$，均有$f(n\lambda_0x)=nf(\lambda_0x)=n\lambda_0f(x)+nd$，'),
            Tex(r'又因为$f(n\lambda_0x)\le n\lambda_0f(x)+c$，所以$nd\le c$'),
            Tex(r'令$n\to+\infty$或$n\to-\infty$可得到矛盾'),
        ).arrange(DOWN,.2,aligned_edge = LEFT).to_edge(LEFT,1.4)
        g.add(prf)

        self.play(Write(prf),run_time=5)
        self.wait(10)
        self.play(FadeOut(g))                                             

    def condition2(self):
        g = VGroup()
        condition = Tex(r'(2)$f(x)$在$x=x_0$处连续')
        condition.next_to(self.tex2,DOWN,.3,LEFT)
        self.play(Write(condition))
        self.wait(2)
        g.add(condition)
        self.condition2_text = condition

        prf1 = VGroup(
            Tex(r'对任意实数$x_1$，设$d=x_1-x_0$，\\则$f(x_1)=f(d)+f(x_0)$，那么'),
            MathTex('f(x_1)=','f(x_0)+f(d)')
        ).arrange(DOWN,.2,aligned_edge=LEFT)
        prf1.next_to(condition,DOWN,.3,LEFT,)
        self.play(Write(prf1))
        self.wait(2)
        lim = r'\lim\limits_{x\to x_0}'
        prf1_2s = [
            MathTex(r'f(x_1)=',lim,'f(x)+','f(d)'),
            MathTex(r'f(x_1)=',lim,'[f(x)+','f(d)]'),
            MathTex(r'f(x_1)=',lim,'f(x+d)',''),
            MathTex(r'f(x_1)=',r'\lim\limits_{x\to x_1}','f(x)'),
        ]
        prf1_2 = prf1[1]
        for item in prf1_2s:
            item.next_to(prf1_2,DOWN,.2,LEFT)
            self.play(ReplacementTransform(prf1_2.copy(),item))
            
            prf1_2 = item
            self.wait(1.5)
            g.add(item)

        prf1_3 = Tex(r'，从而$f(x)$处处连续')
        prf1_3.next_to(prf1_2,RIGHT,.2)
        self.play(Write(prf1_3))
        self.wait(3)
        g.add(prf1,prf1_3)

        prf2 = VGroup(
            Tex(r'对任意无理数$\lambda$，'),
            Tex(r'存在一个收敛于$\lambda$的无穷有理数列$\{q_n\}$'),
            MathTex(r'f(\lambda x)=\lim\limits_{n\to\infty}f(q_n x)'),
        ).arrange(DOWN,.2,aligned_edge=LEFT).next_to(prf1,RIGHT,1.5,UP)
        prf2_2s = [
            MathTex(r'f(\lambda x)=',r'\lim\limits_{n\to\infty}q_n',r'\cdot f(x)'),
            MathTex(r'f(\lambda x)=',r'\big(\lim\limits_{n\to\infty}q_n\big)',r'\cdot f(x)'),
            MathTex(r'f(\lambda x)=',r'\lambda',r'\cdot f(x)'),
        ]
        self.play(Write(prf2))
        g.add(prf2)
        self.wait(2)
        prf2_2 = prf2[2]
        for item in prf2_2s:
            item.next_to(prf2_2,DOWN,.2,LEFT)
            self.play(ReplacementTransform(prf2_2.copy(),item))
            
            prf2_2 = item
            self.wait(1.5)
            g.add(item)


        self.wait(7)
        self.play(FadeOut(g))


    def conclusion(self):
        self.condition2_text.next_to(self.condition2_text,DOWN,.3,LEFT)
        self.play(Write(self.condition1_text))
        self.play(Write(self.condition2_text))
        c3 = Tex(r'(3)$f(x)$是单调函数')
        c3.next_to(self.condition2_text,DOWN,.3,LEFT)
        self.wait(2)
        con = Tex('有理数$q\\to$实数$\\lambda$')
        con.next_to(c3,DOWN,.5,LEFT)
        self.play(Write(con))
        self.wait(1)
        self.play(Write(c3))
        self.wait(3)


'''
f(x)+f(y)=f(x+y)这样的方程是柯西方程，
本期视频会研究这个函数的性质.
我们先行代入特殊值，可以得到f是奇函数，
接下来，我们可以通过归纳证明括号内的整数可以提出到括号外，
再通过变形可以将整数推广到有理数，

那么，能否将有理数再次推广到实数范围呢？
很遗憾，这并不一定是正确的，
既然如此，那么我们可以尝试添加一些条件来让其成立.

第一个想法是给f一个不等式来限定，
画出图像不难发现f的图像一定在黄色直线的下方，
假设有一个点偏离了原来的直线，
这个点也会去确定一条新的直线，
如粉点所示，
现在注意看被黄色框圈起的点，
它已经超出了黄色线的范围，
这就造成了矛盾！
从而可以断言所有点都要在原直线上，
接着就可以写出其完整的证明.

第二个想法是够使f某点连续，
由条件可以先进一步推出f处处连续，
这样在主观上它很可能是一条直线，
对于某个无理数λ，
我们可以找到其有理序列逼近，
再将有理数提出，
经过变形就能够得到最终的结论.

本期我们得到了满足这一方程的f的基本性质，
同时增加了一些条件将f确定为一条直线，
对于第三个想法：f是单调函数，
将在下期进行讨论.

'''