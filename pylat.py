import _ast
import ast
import sys

#ast transformer
class MyTransformer(ast.NodeTransformer):

    def __init__(self):
        super(MyTransformer, self).__init__()
        self.result = []

    def iterate_children(self, node):
        """
        helper
        """
        children = ast.iter_child_nodes(node)
        for c in children:
            self.visit(c)

    def generic_visit(self, node):
        """
        default behaviour
        """
        super().generic_visit(node)
        print("visiting: " + node.__class__.__name__)
        return node

    def visit_For(self, node):
        """
        For nodes: replace with nothing
        """
        print("Found a For node!")
        print(node)
        return super().generic_visit(node)

    def visit_BinOp(self, node):
        print("BinOp", node.op)
        if type(node.op).__name__ == "Pow":
          self.result.append("**")
        return super().generic_visit(node)   

    def visit_Num(self, node):
        print("Num", node.n)
        self.result.append(node.n)
        return super().generic_visit(node)

    def visit_Name(self, node):
        print("Name", node.id)
        self.result.append(node.id)
        return super().generic_visit(node)    

    def spit(self):
        return self.result




#compile source to ast
m = compile("x ** 2", "<string>", "exec", _ast.PyCF_ONLY_AST)

#do ast manipulation
t = MyTransformer()
t.visit(m)

# fix locations
#m = ast.fix_missing_locations(m)

#visualize the resulting ast
#p = AstPrinter()
#p.fromAst(m)

#execute the transformed program
#print("computing...")
#codeobj = compile(m, '<string>', 'exec')
#exec(codeobj)