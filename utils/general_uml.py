import ast
import os
import subprocess


class UMLGenerator(ast.NodeVisitor):
    def __init__(self):
        self.classes = {}
        self.relations = []

    def visit_ClassDef(self, node):
        """Sınıfları ve ilişkilerini analiz et"""
        class_name = node.name
        methods = []
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                methods.append(item.name)
            elif isinstance(item, ast.Assign):
                # Sınıflar arası ilişki varsa tespit et
                for target in item.targets:
                    if isinstance(target, ast.Name) and isinstance(
                        item.value, ast.Call
                    ):
                        if isinstance(item.value.func, ast.Name):
                            self.relations.append((class_name, item.value.func.id))
        self.classes[class_name] = methods
        self.generic_visit(node)

    def generate_puml(self, output_file):
        """Tek bir UML dosyası oluştur"""
        with open(output_file, "w") as uml:
            uml.write("@startuml\n")
            for class_name, methods in self.classes.items():
                uml.write(f"class {class_name} {{\n")
                for method in methods:
                    uml.write(f"  + {method}()\n")
                uml.write("}\n")
            # Sınıf ilişkilerini ekle
            for parent, child in self.relations:
                uml.write(f"{parent} --> {child}\n")
            uml.write("@enduml\n")


def process_directory(input_dir, output_file, plantuml_path):
    generator = UMLGenerator()

    # Klasördeki tüm Python dosyalarını analiz et
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".py"):
                input_file = os.path.join(root, file)
                with open(input_file, "r", encoding="utf-8") as source:
                    tree = ast.parse(source.read())
                    generator.visit(tree)

    # Tek bir UML dosyası oluştur
    generator.generate_puml(output_file)

    # PlantUML ile diyagramı oluştur
    subprocess.run(["java", "-jar", plantuml_path, output_file], check=True)
    print(f"UML diyagramı {output_file.replace('.puml', '.png')} olarak oluşturuldu.")


# Kullanıcı girdisi
input_directory = "../"  # Python dosyalarının olduğu klasör
output_file = "./uml_diagram.puml"
plantuml_jar_path = "./plantuml-mit-1.2024.8.jar"

process_directory(input_directory, output_file, plantuml_jar_path)
