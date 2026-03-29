from manim import *

class MyScene(Scene):
    def construct(self):
        Text.set_default(font_size=20,font="SimSong")
        MathTex.set_default(font_size=27)
        self.show_question()
        self.solve()
        
    def show_question(self):
        question = VGroup(Text('在实数范围内解方程：'),MathTex(r'x^{10}','+','5x^8','-','4x^5','-','5x^2','-','1','=0.'))
        question.arrange(DOWN,.2,aligned_edge=LEFT)
        question.scale(1.6)
        question.set_color(YELLOW)
        self.play(Write(question))
        self.wait(5)
        self.question = question
        self.play(question.animate.scale(.7).arrange(RIGHT,.2).to_edge(UL,1))
        self.wait(1)

    def solve(self):
        tex = self.question[1]
        # 创建高亮框
        box = []
        for i in range(2):
            temp = [SurroundingRectangle(tex[2*i]),SurroundingRectangle(tex[8-2*i])]
            if len(box) > 0:
                self.play(ReplacementTransform(box[0],temp[0]),ReplacementTransform(box[1],temp[1]))
            else:
                self.play(Create(temp[0]),Create(temp[1]))
            box = temp
            self.wait(1)
        self.play(FadeOut(box[0]),FadeOut(box[1]))
        self.wait(2)


        l1 = VGroup(Text('注意到'),MathTex('x=0'),Text('不是原方程的根'),Text('，则原方程等价于'),MathTex(r'x^5-\frac{1}{x^5}+5\Big(x^3-\frac{1}{x^3}\Big)-4=0')).arrange(RIGHT).next_to(self.question,DOWN,.4,LEFT)
       
        self.play(Write(l1[0:3]))
        self.wait(1)
        self.play(Write(l1[3:]),run_time=2)
        self.wait(2)

        l2 = VGroup(
            Text('令'),MathTex(r't=x-\frac1x'),
            Text('，则有'),MathTex(r'x^3-\frac{1}{x^3}=t^3+3t,x^5-\frac1{x^5}=t^5+5t^3+5t'),
        ).arrange(RIGHT,buff=.1).next_to(l1,DOWN,.2,LEFT)
        self.play(Write(l2[0:2]))
        self.wait(1)
        self.play(Write(l2[2:4]))
        self.wait(2)

        l2_ = VGroup(
            Text('则原方程等价于'),MathTex('t^5+10t^3+20t-4=0')
        ).arrange(RIGHT,buff=.1).next_to(l2,DOWN,.2,LEFT)
        self.play(Write(l2_ ))
        self.wait(5)

        # 换元尝试
        def try_step():
            nl1 = VGroup(Text('尝试作换元'),MathTex('t=a+b')).arrange(RIGHT)
            nl2 = VGroup(Text('则原方程等价于'),MathTex('a^5+b^5+','5(a^4b+ab^4)+10(a^3b^2+a^2b^3)+10(a+b)^3+20(a+b)','-4=0')).arrange(RIGHT)
            nl3 = VGroup(Text('希望'),nl2[1][1].copy(),MathTex('=0')).arrange(RIGHT,0.1)
            nl4 = VGroup(Text('计算得到：'),MathTex(r'\text{LHS}=5(a+b)(ab+2)(a^2+b^2+ab+2)=0')).arrange(RIGHT,.2)
            nl5 = VGroup(Text('此时只需'),MathTex('ab=-2'),Text('即'),MathTex(r'b=-\frac2a'),Text('即可')).arrange(RIGHT,.2)
            
            g = VGroup(nl1,nl2,nl3,nl4,nl5).set_color(PINK).arrange(DOWN,.1,aligned_edge=LEFT)
            g.next_to(l2_,DOWN,.3,LEFT)
            

            self.play(Write(nl1))
            self.wait(1)
            self.play(Write(nl2))
            self.wait(1)
            box = SurroundingRectangle(nl2[1][1])
            self.play(Create(box))
            self.wait(1)
            cpy = nl2[1][1].copy()
            self.play(Write(nl3[0]),cpy.animate.move_to(nl3[1]),Write(nl3[2]),FadeOut(box))
            nl3[1] = cpy
            self.wait(1)
            self.play(Write(nl4))
            self.wait(1)
            self.play(Write(nl5))
            self.wait(5)
            self.play(FadeOut(g))

        try_step()

        l3 = VGroup(
            Text('再令'),MathTex(r't=a-\frac2a'),
            Text('，则原方程等价于'),MathTex(r'a^5-\frac{32}{a^5}=4'),
            Text('，或等价于'),MathTex(r'(a^5)^2-4a^5-32=0')
        ).arrange(RIGHT,buff=.1).next_to(l2_,DOWN,.2,LEFT)
        self.play(Write(l3[:2]))
        self.wait(1)
        self.play(Write(l3[2:4]))
        self.wait(1)
        self.play(Write(l3[4:]))
        self.wait(2)

        l4 = VGroup(
            Text('解得'),MathTex(r'a^5=-4'),Text('或'),MathTex(r'a^5=8'),
            Text('，则'),MathTex(r'a=-2^{2/5}'),Text('或'),MathTex(r'a=2^{3/5}'),
            Text('，两种情况均得到'),
            MathTex(r't=2^{3/5}-2^{2/5}')
        ).arrange(RIGHT,.1).next_to(l3,DOWN,.2,LEFT)
        self.play(Write(l4[:4]))
        self.wait(1)
        self.play(Write(l4[4:8]))
        self.wait(2)
        self.play(Write(l4[8:]))
        self.wait(2)

        l5 = VGroup(
            Text('又由于'),MathTex(r't=x-\frac1x'),
            Text('即'),
            MathTex('x^2-tx-1=0')
        ).arrange(RIGHT,.1).next_to(l4,DOWN,.2,LEFT)
        self.play(Write(l5))
        self.wait(1)

        m1 = MathTex(r'x=\frac{t\pm\sqrt{t^2+4}}{2}')
        m2 = MathTex(r'x=\frac{2^{3/5}-2^{2/5}\pm\sqrt{(2^{3/5}-2^{2/5})^2+4}}{2}')
        m3 = MathTex(r'x=\frac{2^{3/5}-2^{2/5}\pm\sqrt{2^{4/5}+2^{6/5}}}{2}')
        l6 = VGroup(
            Text('解得'),m2
        ).arrange(RIGHT,.1).next_to(l5,DOWN,.2,LEFT)
        l6[1] = m1
        m1.move_to(m2,LEFT)
        m3.move_to(m2,LEFT)
        self.play(Write(l6))
        self.wait(1)
        self.play(ReplacementTransform(m1,m2))
        self.wait(1)
        self.play(ReplacementTransform(m2,m3))
        m4 = (MathTex(r'x_1\approx 1.10291,\;x_2\approx -0.906696')).next_to(l6,RIGHT,.3)
        self.play(Write(m4))
