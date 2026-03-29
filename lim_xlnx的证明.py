from manim import *


config.tex_template = TexTemplateLibrary.ctex


class Limitxlnx(Scene):
    def construct(self):
        #设置字体字号
        Text.set_default(font_size=20,font="SimSong")
        MathTex.set_default(font_size=27)

        self.introduce()
        self.wait(2)
        self.another()

    def introduce(self):  

        self.tex1 = Tex('设$f(x)=x\\ln x$，求$\\lim\\limits_{x\\to0^+}f(x)$.').scale(1.4).set_color(YELLOW)
        self.play(Create(self.tex1))
        self.wait(2)

        # self.tex1.to_edge(UL,.6)/
        self.play(self.tex1.animate.shift([0,1.8,0]),run_time=1)

        lHôpital_solution = MathTex(r'''
            \lim_{x\to0^+}x\ln x &=\lim_{x\to0^+}\frac{\ln x}{1/x} \\
                            &= \lim_{x\to0^+}\frac{1/x}{-1/x^2}\\
                            &= \lim_{x\to0^+}-x \\
                            &= 0
        ''')
        self.play(Write(lHôpital_solution),run_time=2)

        self.wait(2)

        self.play(Unwrite(lHôpital_solution),self.tex1.animate.to_edge(UP,.8),run_time=1)

    def another(self):
        equal = MathTex(r"\Leftrightarrow\forall \varepsilon>0,\; \exists \delta>0,\; \forall x\in(0,\delta),\: |f(x)|<\varepsilon")
        equal.next_to(self.tex1,DOWN,.4)
        self.play(Write(equal))

        self.wait(2)

        monotonicity = VGroup(
            Tex("由$f'(x)=\ln x+1$，"),
            Tex('则$f(x)$在$\\left(0,\\dfrac1{\\mathrm{e}}\\right)$上单调递减，'),
            Tex('在$\\left(\\dfrac1{\\mathrm{e}},+\\infty\\right)$上单调递增.'),
            
        ).arrange(RIGHT,.2)

        monotonicity.next_to(equal,DOWN,.3)
        self.play(Write(monotonicity[0]))
        self.wait(.3)
        self.play(Write(monotonicity[1:3]))
        self.wait(1)
        # s.play(Write(monotonicity[3]))
        # ranges = Tex(r'故$f(x)\ge f\left(\dfrac{1}{\mathrm{e}}\right)=-\dfrac{1}{\mathrm{e}}$.')
        ranges = VGroup(
            Tex(r'故$f(x)\ge f\left(\dfrac{1}{\mathrm{e}}\right)=-\dfrac{1}{\mathrm{e}}$，'),
            Tex(r'且当$x\in(0,1)$时，$f(x)<0$.')
        ).arrange(RIGHT,.2).next_to(monotonicity,DOWN,.2,ORIGIN)

        self.play(Write(ranges[0]))
        self.wait(1)
        self.play(Write(ranges[1]))
        self.wait(3)
        final = self.mainInequality(ranges);
        
        # instruction = Tex('(当且仅当$x=\\dfrac{1}{\\mathrm{e}^2}$时取等)').next_to(final,RIGHT,.2)
        # self.play(Write(instruction))
        self.wait(3)

        set_delta = Tex(
            r'回到原题，对任意的$\varepsilon>0$，',
            r'令$\delta=\min\left\{1,\dfrac{\mathrm{e}^2\varepsilon^2}{4}\right\}$，',
            r'则对任意$x\in (0,\delta)$有'
        ).next_to(final,DOWN,.2)
        # self.play(Write(set_delta[0]))
        # self.wait(.3)
        # self.play(Write(set_delta[1]))
        # self.wait(.3)
        # self.play(Write(set_delta[2]))s
        self.play_slice(set_delta,.3)
        self.wait(1)

        conclusion = MathTex(
            r'f(x)<0,',
            r'f(x)\ge-\frac{2\sqrt{x}}{\mathrm{e}}>-\frac{2\sqrt{\frac{\mathrm{e}^2\varepsilon^2}{4}}}{\mathrm{e}}=-\varepsilon',
            r'\Rightarrow |f(x)|<\varepsilon'
        ).next_to(set_delta,DOWN,.2)
        # self.play(Write(conclusion[0]))
        self.play_slice(conclusion,.4)
        self.wait(4)

        

    def mainInequality(self,below:Mobject) -> Mobject:
        
        current = self.emph(MathTex('x','\\ln x','\\ge', '-\\frac{1}{\\mathrm{e}}',r'\;(\forall x\in(0,+\infty))'))
        current.next_to(below,DOWN,.3)
        self.play(Write(current))
        self.wait(1)
        
        # second = self.emph(MathTex('x^2','\\ln x','\\ge', '-\\frac{x}{\\mathrm{e}}',r'\;(\forall x\in(0,+\infty))'))
        # self.move_and_transform(current,second)

        current = self.move_and_transform(current ,self.emph(MathTex('x^2','\\ln x','\\ge', '-\\frac{x}{\\mathrm{e}}',r'\;(\forall x\in(0,+\infty))')))

        current = self.move_and_transform(current, self.emph(MathTex('x^2',r'\left(\frac12\ln x^2\right)','\\ge', '-\\frac{x}{\\mathrm{e}}',r'\;(\forall x\in(0,+\infty))')))

        current = self.move_and_transform(current, self.emph(MathTex('x^2',r'\ln x^2','\\ge', '-\\frac{2x}{\\mathrm{e}}',r'\;(\forall x\in(0,+\infty))')))
        change = Tex(r'令$t=x^2$，则$x=\sqrt{t}$').next_to(current,DOWN,.2)
        self.play(Write(change))

        current = self.move_and_transform(current, self.emph(MathTex('t',r'\ln t','\\ge', '-\\frac{2\\sqrt{t}}{\\mathrm{e}}',r'\;(\forall t\in(0,+\infty))')))
        self.play(Uncreate(change))


        current = self.move_and_transform(current, self.emph(MathTex('x',r'\ln x','\\ge', '-\\frac{2\\sqrt{x}}{\\mathrm{e}}',r'\;(\forall x\in(0,+\infty))')))

        return current

        
        

    def emph(self,mobj:Mobject) -> Mobject:
        return mobj.scale(1.2).set_color(PINK)
    
    def move_and_transform(self,origin:Mobject,target:Mobject,aligned_edge=ORIGIN) ->Mobject :
        target.move_to(origin,aligned_edge)
        self.play(ReplacementTransform(origin,target))
        self.wait(1)
        return target
    
    def play_slice(self,arr,duration = 1):
        for v in arr :
            self.play(Write(v))
            self.wait(duration)



'''
对于屏幕上所示的这个极限，我们可以通过变形后使用洛必达法则可以得到其极限值为0，本期视频我们将使用高中范围内的知识来解决这个极限值是0的证明。

首先，我们先利用极限的的定义写出原命题的等价形式，将极限转换为一种不等关系。
接着我们对f x求导，就可以得到f(x)的单调性，并利用单调性得到它的最小值。

我们注意这个最小值中蕴含的不等式，现在它还无法让我们完成证明，因为我们希望右侧的极限值也是0，
因此我们可以在不等式两边同乘x，再利用对数公式改写式子。最后经过整理，就可以得到一个满足我们期望的不等式了。

最后我们来考虑δ的选取，首先让其不大于1来使得函数值是负的，再通过刚才的不等式能够解出另一个要求，两者结合就完成了δ的选取。
选取完毕δ后就可以根据刚刚证明的不等式得到最后的结论成立。
'''