from manim import *

config.tex_template = TexTemplateLibrary.ctex
class Algebra(Scene):
    def construct(self):
        #设置字体字号
        Text.set_default(font_size=28,font="SimSong")
        Tex.set_default(font_size=30)
        MathTex.set_default(font_size=30)
        self.introduce()
        self.two_var_solution()
        self.show_lemma()
        self.show_summary()
    
    def introduce(self):
        self.title = Tex(r'设$n$为正整数，实数$a_1,a_2,\ldots,a_n\in(0,1)$，'+'\n\n'+r'证明：$a_1^{a_1}+a_2^{a_2}+\cdots+a_n^{a_n}\ge a_1^{a_2}+a_2^{a_3}+\cdots+a_{n-1}^{a_n}+a_n^{a_1}$.').scale(1.2).set_color(YELLOW)
        self.play(Create(self.title))
        self.wait(5)
        self.play(self.title.animate.to_edge(UP,.7))

    def two_var_solution(self):
        two_var_q = Tex(r'设实数$a,b\in(0,1)$，证明：$a^a+b^b\ge a^b+b^a$.')
        two_var_q.next_to(self.title,DOWN,.3,ORIGIN)
        self.play(Write(two_var_q))
        self.wait(3)
        choices = VGroup(MathTex(r'a^a-a^b\ge b^a-b^b'),MathTex(r'a^a-b^a\ge a^b-b^b')).arrange(RIGHT,.6)
        choices.next_to(two_var_q,DOWN,.4)
        self.play(Write(choices))
        self.wait(2)
        box = SurroundingRectangle(choices[0])
        self.play(Create(box))
        self.wait(1)

        # func = 
        # dif = 
        func = VGroup(
            Tex(r'不妨假设$a>b$($a=b$时结论显然成立)，设$f(x)=x^a-x^b$，'),
            VGroup(
                Tex(r"则当$x\in[b,a]$时，","$f'(x)=ax^{a-1}-bx^{b-1}$"),
                Tex(r"$=bx^{b-1}\Big(\dfrac{a}{b}x^{a-b}-1\Big)$"),
                Tex(r'$\ge$'),
                Tex(r"$bx^{b-1}\Big(\dfrac{a}{b}b^{a-b}-1\Big)$")
            ).arrange(RIGHT,.1),
        ).arrange(DOWN,.3,aligned_edge=LEFT)
        func.next_to(box,DOWN,.3).to_edge(LEFT,.5)
        self.play(Write(func[0]),Uncreate(box))
        self.wait(2)
        self.play(Write(func[1]),run_time=2)
        self.wait(2)

        box = SurroundingRectangle(func[1][3])
        self.play(Create(box))
        self.wait(2)
        self.play(Uncreate(box))

        gx = VGroup(
            Tex(r"设$g(x)=x\cdot b^{x-b-1}$，"),
            Tex(r"则$g'(x)=b^{x-b-1}(x\ln b+1)$"),
        ).arrange(RIGHT,.1)
            
        gx.next_to(func,DOWN,.2).to_edge(LEFT,.5)
        self.play(Write(gx[0]))
        self.wait(1)
        self.play(Write(gx[1]))
        self.wait(2)
        gdx=Tex(r"则$g(x)$在$\Big(0,-\dfrac{1}{\ln b}\Big)$上单调递增，在$\Big(-\dfrac{1}{\ln b},+\infty\Big)$上单调递减")
        gdx.next_to(gx,DOWN,.2,LEFT)
        self.play(Write(gdx))
        self.wait(2)
        res = VGroup(
            Tex(r"由于$a\in(b,1)$，则$g(a)>\min\{g(b),g(1)\}$"),
            Tex(r"又$g(b)=1,g(1)=\frac{1}{b^b}>1$，则$g(a)>1$，"),
        ).arrange(RIGHT,.1)
        res.next_to(gdx,DOWN,.2,LEFT)
        self.play(Write(res),run_time=2)
        self.wait(3)

        func_before = func[1][0][0]
        func_after = Tex(r"则当$x \ge b$时，").move_to(func_before,RIGHT)
        self.play(Transform(func_before,func_after))
        self.wait(2)

        back = VGroup(
            Tex(r"从而此时$f'(x)>0$，则$f(x)$在$[b,+\infty)$上单调递增，"),
            Tex(r'故$f(a)>f(b)$，结论成立.'),
        ).arrange(RIGHT,.1).next_to(res,DOWN,.2,LEFT)
        self.play(Write(back[0]))
        self.wait(2)
        self.play(Write(back[1]))
        self.wait(5)
        self.play(Uncreate(VGroup(
            two_var_q,choices,func_after,func,gx,gdx,res,back
        )),run_time=1)
        self.wait(1)

    def show_lemma(self):
        self.lemma = Tex(r'引理：对$f(x)=x^a-x^b(a>b)$，$f(x)$在$[b,+\infty)$上单调递增.')
        self.lemma.next_to(self.title,DOWN,.3)
        self.play(Write(self.lemma))
        self.wait(2)

    def show_summary(self):
        summary_topic =VGroup(
            Tex(r'对$n$归纳证明，$n=2$时成立，'),
            Tex('假设$n=k$时成立， 考虑$n=k+1$时，'),
        ).arrange(RIGHT,.2).next_to(self.lemma,DOWN,.2).to_edge(LEFT,.5)
        self.play(Write(summary_topic))
        self.wait(2)

        analyze = VGroup(
            Tex(r'已经有：$a_1^{a_1}+a_2^{a_2}+\cdots+a_k^{a_k}\ge a_1^{a_2}+a_2^{a_3}+\cdots+a_{k-1}^{a_k}+a_k^{a_1}$'),
            Tex(r'结论为：$a_1^{a_1}+a_2^{a_2}+\cdots+a_{k+1}^{a_{k+1}}\ge a_1^{a_2}+a_2^{a_3}+\cdots+a_{k-1}^{a_k}+a_k^{a_{k+1}}+a_k^{a_1}$')
        ).arrange(DOWN,.2,aligned_edge=LEFT).next_to(summary_topic,DOWN,.2,LEFT)
        self.play(Write(analyze),run_time=2)
        self.wait(2)

        goal = Tex(r'只需证明：$a_{k+1}^{a_{k+1}}\ge a_k^{a_{k+1}}+a_k^{a_1}-a_k^{a_1}$，',r'即$a_k^{a_1}-a_k^{a_{k+1}}\ge a_{k+1}^{a_1}-a_{k+1}^{a_{k+1}}$')
        goal.next_to(analyze,DOWN,.2,LEFT)
        self.play(Write(goal[0]))
        self.wait(1)
        self.play(Write(goal[1]))
        self.wait(2)

        solution = VGroup(
            Tex(r'不妨设$a_{k+1}$最小，则由引理知$f(x)=x^{a_1}-x^{a_{k+1}}(a_1\ge a_{k+1})$'),
            Tex(r'在$[a_{k+1},+\infty)$上单调不减，')
        ).arrange(RIGHT,.2).next_to(goal,DOWN,.2,LEFT)
        self.play(Write(solution))
        self.wait(2)

        end = Tex(r'则$f(a_k)\ge f(a_{k+1})$，所以$n=k+1$时也成立，由数学归纳法知结论成立.')
        end.next_to(solution,DOWN,.2,LEFT)
        self.play(Write(end))
