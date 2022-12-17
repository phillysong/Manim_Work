from manim import *
from manim.utils.color import Colors
import random
import datetime




def generate_fixed_id():
    random_fixed_id=random.randint(400000,999999)
    return random_fixed_id
import datetime



%%manim -qm -v WARNING Profile_Card

class Profile_Card(Scene):
    
    def construct(self):
        fixed_id_date=Text('2022-04-10',font_size=26)
        
        top_profile_rectangle=Rectangle(width=14,height=1.5,).scale(.3)
        left_profile_rectangle=Rectangle(width=5,height=9,).scale(.3)
        right_profile_rectangle=Rectangle(width=9,height=9,).scale(.3)
        
        left_profile_rectangle.next_to(top_profile_rectangle,DL, buff=0).shift(left_profile_rectangle.width*RIGHT)
        right_profile_rectangle.next_to(top_profile_rectangle,DR, buff=0).shift(right_profile_rectangle.width*LEFT)
        initial_profile_card=Group(top_profile_rectangle,left_profile_rectangle,right_profile_rectangle).shift(UP*1.5)
        self.add(top_profile_rectangle,initial_profile_card)
#         self.wait(1)
        self.play(ScaleInPlace(initial_profile_card,2))
#         self.wait(2)

        empty_profile = ImageMobject(r'D:\Manim_Scripts\Manim_external_photos\empty_profile.png').move_to(left_profile_rectangle.get_center())
        fixed_id=generate_fixed_id()
        profile_card_header=Text(f'Fixed ID: {fixed_id}',font_size=26).move_to(top_profile_rectangle.get_center())
        fixed_id_date.move_to(empty_profile.get_center()).shift(DOWN*1.2)
        card_text1=Text('2021-10-13: CPT 99327',font_size=23)
        card_text2=Text('2021-11-15: CPT 99212',font_size=23)
        card_text3=Text('2022-01-26: Diagnosis E114',font_size=23)
        card_text4=Text('2022-01-28: Filled drug d05896',font_size=23)
        card_text5=Text('2022-03-02: CPT 95249',font_size=23)
        card_text6=Text('2022-04-06: Filled drug d05896',font_size=23)
        card_text7=Text('2022-04-12: Diagnosis J41.1',font_size=23)
        card_text8=Text('2022-07-23: Diagnosis I15.2',font_size=23)
        card_text9=Text('2022-08-09: Filled drug d04743',font_size=23)
        card_text10=Text('2022-08-14: Filled drug d08290',font_size=23)
        card_text11=Text('2022-09-15: CPT 95249',font_size=23)

        profile_card_text=Group(card_text1,card_text2,card_text3,card_text4,card_text5,card_text6,card_text7,card_text8,card_text9,card_text10,card_text11).arrange(DOWN,center=False, aligned_edge=LEFT,buff=.15).shift(RIGHT*.85,UP*2)
        Card_text_animation_group=AnimationGroup(Write(card_text1),
                                    Write(card_text2),
                                    Write(card_text3),
                                    Write(card_text4),
                                    Write(card_text5),
                                    Write(card_text6),
                                    Write(card_text7),
                                    Write(card_text8),
                                    Write(card_text9),
                                    Write(card_text10),
                                    Write(card_text11),
                                    lag_ratio=0.2)
        self.play(FadeIn(empty_profile,fixed_id_date,profile_card_header))
        self.play(Card_text_animation_group)
        
        raw_dates_text=Text('Raw dates are translated to datediffs relative to the Exposure Date',font_size=28).next_to(left_profile_rectangle,DOWN).shift(RIGHT*2.5)
        self.play(Write(raw_dates_text))
        self.wait(1)
        self.play(Indicate(fixed_id_date),color=RED_A)
        
        
        transaction_list=[card_text1,card_text2,card_text3,card_text4,card_text5,card_text6,card_text7,card_text8,card_text9,card_text10,card_text11]
        card_text1_changed=Text('-179: CPT 99327',font_size=23,color=GOLD_E)
        card_text2_changed=Text('-146: CPT 99212',font_size=23,color=GOLD_E)
        card_text3_changed=Text('-74: Diagnosis E114',font_size=23,color=GOLD_E)
        card_text4_changed=Text('-72: Filled drug d05896',font_size=23,color=GOLD_E)
        card_text5_changed=Text('-39: CPT 95249',font_size=23,color=GOLD_E)
        card_text6_changed=Text('-4: Filled drug d05896',font_size=23,color=GOLD_E)
        card_text7_changed=Text('2: Diagnosis J41.1',font_size=23,color=TEAL_A)
        card_text8_changed=Text('104: Diagnosis I15.2',font_size=23,color=TEAL_A)
        card_text9_changed=Text('121: Filled drug d04743',font_size=23,color=TEAL_A)
        card_text10_changed=Text('126: Filled drug d08290',font_size=23,color=TEAL_A)
        card_text11_changed=Text('158: CPT 95249',font_size=23,color=TEAL_A)
        profile_card_text_changed=Group(card_text1_changed,card_text2_changed,card_text3_changed,card_text4_changed,card_text5_changed,card_text6_changed,card_text7_changed,card_text8_changed,card_text9_changed,card_text10_changed,card_text11_changed).arrange(DOWN,center=False, aligned_edge=LEFT,buff=.15).shift(RIGHT*.85,UP*2)
        
        card_text_change_dict={
                                card_text1:card_text1_changed,
                                card_text2:card_text2_changed,
                                card_text3:card_text3_changed,
                                card_text4:card_text4_changed,
                                card_text5:card_text5_changed,
                                card_text6:card_text6_changed,
                                card_text7:card_text7_changed,
                                card_text8:card_text8_changed,
                                card_text9:card_text9_changed,
                                card_text10:card_text10_changed,
                                card_text11:card_text11_changed
                                }
        
        fixed_id_date.set_color(RED_B)
        for i in range(len(transaction_list)):
            fixed_id_date.generate_target()
            fixed_id_date.target.next_to(transaction_list[i],LEFT).shift(LEFT*.2)
            self.play(MoveToTarget(fixed_id_date),Transform(transaction_list[i],card_text_change_dict[transaction_list[i]]),run_time=.44)
            self.wait(.1)
        