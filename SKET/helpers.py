screen_helper = """
ScreenManager:
    FileInput:
    AxisSelector:
    GraphSelector:
    Display:
    
<FileInput>
    name: 'input'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: app.theme_cls.bg_normal
        
        MDToolbar:
            height: 50
            title: "input"
            margin: 0
            
        ScrollView:
            do_scroll_y: True
            effect_cls: 'ScrollEffect'
            bar_width: 0
            
        MDFloatLayout:
            MDRoundFlatIconButton:
                text: "Choose File"
                icon: "folder"
                pos_hint: {'center_x': .5, 'center_y': .6}
                on_release: app.file_manager_open()
    
<AxisSelector>
    name: 'axis'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: app.theme_cls.bg_normal
        
        MDToolbar:
            height: 50
            title: "axis"
            margin: 0
            left_action_items: [["arrow-left", lambda x: app.rcallback("input")]]

            
        ScrollView:
            do_scroll_y: True
            effect_cls: 'ScrollEffect'
            bar_width: 0
            
    MDBoxLayout:
        orientation: 'vertical'
        pos_hint: {'x' : 0, 'y' : -0.5}
        size: (.5,.5)
        Spinner:
            id: spinner_x
            text: "X axis"
            size_hint: None, None
            size: 200, 44
            pos_hint: {'x' : 0.41, 'y' : 0.5}
            values: []

            
            on_press: root.setx()
            on_text: root.spinnerx_clicked(spinner_x.text)
        
        Spinner:
            id: spinner_y
            text: "Y axis"
            size_hint: None, None
            size: 200, 44
            pos_hint: {'x' : 0.41, 'y' : 0.4}
            values: []
            
            on_press: root.sety()
            on_text: root.spinnery_clicked(spinner_y.text)
            
                
        MDFillRoundFlatButton:
            text: "Generate"
            size_hint: None, None
            size: 100, 44
            pos_hint: {'x' : 0.46, 'y' : 0.4}
            on_press: 
                app.getxy()
                app.lcallback('graphs')
                        
            
        MDFloatLayout:
            pos_hint:{'x': .5, 'y': 1 }
            
            MDLabel:
                md_bg_color: [1,1,1,1]
                text: 'X'
                pos_hint:{'x': .6 , 'y': 1 }
         
    
<GraphSelector>
    name: 'graphs'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: app.theme_cls.bg_normal
        
        MDToolbar:
            height: 50
            title: "Types of graph"
            margin: 0
            left_action_items: [["arrow-left", lambda x: app.rcallback("axis")]]
            
        ScrollView:
            do_scroll_y: True
            effect_cls: 'ScrollEffect'
            bar_width: 0
            
        Spinner:
            id: spinner_graph
            text: "Types"
            size_hint: None, None
            size: 100, 44
            pos_hint: {'center_x': .5, 'center_y': .5}
            values: ["scatter plot", "bar graph", "line graph"]
            on_text: root.spinner_graph_clicked(spinner_graph.text)
                
                
        MDFillRoundFlatButton:
            text: "Generate"
            size_hint: None, None
            size: 100, 44
            pos_hint: {'x' : 0.445, 'y' : 0.4}
            on_press: 
                app.graph()
                app.lcallback("disp")
        
        MDLabel:
        
            
    
<Display>
    name: 'disp'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: app.theme_cls.bg_normal
        
        MDToolbar:
            height: 50
            title: "disp"
            margin: 0
            left_action_items: [["arrow-left", lambda x: app.rcallback("graphs")]]
            right_action_items: [["reload", lambda x : root.img_refresh()]]
            
        ScrollView:
            do_scroll_y: True
            effect_cls: 'ScrollEffect'
            bar_width: 0
            
        MDBoxLayout:
            orientation: 'vertical'
            size_hint: (1,100)
            Image:
                id: img
                allow_stretch: True
                keep_ratio: True
"""
