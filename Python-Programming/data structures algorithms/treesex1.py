class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_tree(self):
        spaces='    '*self.get_level()*3
        prefix=spaces+'|__'if self.parent else '   '
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
def build_tree():
    root=TreeNode('Tollywood')

    heroin=TreeNode('Heroins')
    heroin.add_child(TreeNode('Samantha'))
    heroin.add_child(TreeNode('RakulPsing'))
    heroin.add_child(TreeNode('Pooja'))

    hero=TreeNode('Heros')
    hero.add_child(TreeNode('AlluArjun'))
    hero.add_child(TreeNode('RajiniMuragan'))
    hero.add_child(TreeNode('PavanKalyan'))

    comedian=TreeNode('Comedians')
    comedian.add_child(TreeNode('Bramha'))
    comedian.add_child(TreeNode('Vkishor'))
    comedian.add_child(TreeNode('ChamakCandra'))

    root.add_child(heroin)
    root.add_child(hero)
    root.add_child(comedian)
    root.print_tree()
if __name__=='__main__':
    build_tree()

    
            
