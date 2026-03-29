from manim import *


class Complex(Scene):
    def construct(self):
        # 默认设置
        Text.set_default(font_size=20,font="SimSong")
        MathTex.set_default(font_size=27)

        self.showTitle()
        self.question()

    # 标题
    def showTitle(self) :
        title = Text('复数范围内的因式分解',font='Microsoft Sans Serif',color=YELLOW).scale(3)
        author = Text('By:gdjt_dsr')
        g = VGroup(title,author).arrange(DOWN,buff=0.8)
        g.move_to(ORIGIN)
        self.play(Write(g))
        self.wait(2)
        self.play(FadeOut(g))
    
    # 题目
    def question(self):
        t1 = MathTex('pa^2+qb^2+rab')
        q_l1 = VGroup(
            Text("设"),
            MathTex(r"S=\{"),
            t1,
            MathTex(r'\;|\;a,b\in\mathbb Z\}'),
            Text('其中常数'),
            MathTex(r'p,q,r'),
            Text('是整数，'),
        ).arrange(RIGHT,buff=.1)
        q_l2 = VGroup(
            Text('证明：若'),
            MathTex(r's_1,s_2\in S'),
            Text('则'),
            MathTex(r'ps_1s_2\in S.')
        ).arrange(RIGHT,buff=.1)
        question1 = VGroup(q_l1,q_l2).arrange(DOWN,aligned_edge=LEFT).scale(1.5)
        self.play(Write(q_l1), run_time=2)
        self.wait(.5)
        self.play(Write(q_l2), run_time=2)
        question2 = VGroup(q_l1.copy(),q_l2.copy()).arrange(RIGHT,buff=.5).scale(.77)
        question2.to_edge(UP,1)
        self.play(Transform(question1,question2))
        self.wait(2)

        t_box = SurroundingRectangle(t1,buff=0.2)
        text1 = Text('因式分解')
        text1.next_to(t_box,DOWN,.2)
        self.play(Create(t_box))
        self.play(Write(text1))
        self.wait(1)
        self.play(FadeOut(text1))
        self.play(Uncreate(t_box))



        eq1 = MathTex(r"pa^2+qb^2+rab=0")
        eq1.next_to(t1,DOWN)
        self.play(Write(eq1))
        eq2 = MathTex(r"p\Big(\frac a b\Big)^2+q+r\Big(\frac a b\Big)=0")
        eq2.move_to(eq1)
        self.play(ReplacementTransform(eq1,eq2))
        self.wait(2)
        eq3 = MathTex(r"px^2+q+rx=0")
        eq3.move_to(eq2)
        self.play(ReplacementTransform(eq2,eq3))
        self.wait(1)
        text2 = VGroup(Text("其必有两复数根"),MathTex(r'x_1,x_2')).arrange(RIGHT,.2,aligned_edge=DOWN)
        text2.next_to(eq3,RIGHT,.4)
        eq3_box = SurroundingRectangle(eq3,buff=.2)
        self.play(Create(eq3_box))
        self.play(Write(text2))
        self.wait(1)

        t2 = MathTex(r'pa^2+qb^2+rab=p(a-x_1b)(a-x_2b)')
        t2.next_to(eq3_box,DOWN)
        self.play(Create(t2))
        self.wait(1)
        self.play(FadeOut(eq3_box,eq3,text2),t2.animate.next_to(t1,DOWN))
        
        self.wait(1)

        t3 = MathTex(r'p','s_1','s_2','=p',r'(pa_1^2+qb_1^2+ra_1b_1)',r'(pa_2^2+qb_2^2+ra_2b_2)')
        t3[1].set_color(BLUE)
        t3[2].set_color(GREEN)
        t3[4].set_color(BLUE)
        t3[5].set_color(GREEN)
        t3.next_to(t2,DOWN,0.3,LEFT)
        self.play(Create(t3))
        self.wait(1)
        t4 = MathTex(r'p','s_1','s_2','=p',r'\cdot',r'p(a_1-x_1b_1)(a_1-x_2b_1)',r'\cdot',r'p(a_2-x_1b_2)(a_2-x_2b_2)')
        t4[5].set_color(BLUE)
        t4[7].set_color(GREEN)
        t4.move_to(t3,LEFT)
        self.play(AnimationGroup(
            ReplacementTransform(t3[4],t4[5]),
            ReplacementTransform(t3[5],t4[7]),
        ))
        self.add(t4[4],t4[6])
        self.wait(2)

        t5 = MathTex('p','(a_1-x_1b_1)','(a_2-x_1b_2)')
        t5.next_to(t4,DOWN,0.4,LEFT)
        t5[1].set_color(BLUE)
        t5[2].set_color(GREEN)
        self.play(Write(t5))
        self.wait(1)
        t6 = MathTex('=pa_1a_2+','px_1^2','b_1b_2-px_1(a_1b_2+a_2b_1)')
        t6.next_to(t5,DOWN,.2,LEFT)
        self.play(Write(t6))
        self.wait(1)

        box1 = SurroundingRectangle(t6[1])
        self.play(Create(box1))
        t6_1 = MathTex("px^2+qx+r=0")
        t6_2 = MathTex("px^2=-qx-r")
        t6_1.next_to(t6,RIGHT,.5)
        t6_2.move_to(t6_1,LEFT)
        self.play(Write(t6_1))
        self.wait(1)
        self.play(ReplacementTransform(t6_1,t6_2))
        self.wait(2)

        t7 = MathTex('=pa_1a_2+','(-qx_1-r)','b_1b_2-px_1(a_1b_2+a_2b_1)')
        t7.next_to(t6,DOWN,.2,LEFT)
        self.play(Write(t7))
        self.play(Uncreate(box1),FadeOut(t6_2))
        self.wait(1)
        t8 = MathTex('=(pa_1a_2-rb_1b_2)-x_1(p(a_1b_2+a_2b_1)+rb_1b_2)')
        t8.next_to(t7,DOWN,.2,LEFT)
        self.play(Write(t8))
        self.wait(3)
        t9 =  MathTex('p','(a_1-x_2b_1)','(a_2-x_2b_2)','=(pa_1a_2-rb_1b_2)-x_2(p(a_1b_2+a_2b_1)+rb_1b_2)')
        t9[1].set_color(BLUE)
        t9[2].set_color(GREEN)
        g9 = VGroup(
            Text('同理'),
            t9
        ).arrange(RIGHT,.2,aligned_edge=DOWN)
        g9.next_to(t8,DOWN,.4,LEFT)
        self.play(Write(g9))
        self.wait(1)
        g10 = VGroup(
            Text("设"),
            MathTex('a_0=pa_1a_2-rb_1b_2\\in\\mathbb{Z},b_0=p(a_1b_2+a_2b_1)+rb_1b_2\\in\\mathbb{Z}')
        ).arrange(RIGHT,.1)
        g10.next_to(g9,DOWN,.2,LEFT)
        self.play(Write(g10))
        
        t3c = t3.copy()
        self.play(t3c.animate.next_to(g10,DOWN,.2,LEFT))
        self.wait(1)
        t31 = MathTex('(a_0-x_1b_0)')
        t32 = MathTex('(a_0-x_2b_0)')
        VGroup(t31,t32).arrange(RIGHT,.1).next_to(t3c[3],RIGHT,.1)
        self.play(ReplacementTransform(t3c[4],t31))
        self.play(ReplacementTransform(t3c[5],t32))
        self.wait(1)
        t11 = MathTex('=','pa_0^2+qb_0^2+ra_0b_0\\in S')
        t11.next_to(t3c[3],DOWN,.2,LEFT)
        self.play(Write(t11))
        self.wait(10)






        
        
