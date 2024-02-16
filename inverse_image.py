from PIL import Image

def inverser_image_horizontal(image_path, save_path):
    # Ouvrir l'image
    image = Image.open(image_path)

    # Inverser horizontalement
    image_inversee = image.transpose(Image.FLIP_LEFT_RIGHT)

    # Sauvegarder l'image inversée
    image_inversee.save(save_path)

def inverser_image_vertical(image_path, save_path):
    # Ouvrir l'image
    image = Image.open(image_path)

    # Inverser verticalement
    image_inversee = image.transpose(Image.FLIP_TOP_BOTTOM)

    # Sauvegarder l'image inversée
    image_inversee.save(save_path)

# Exemple d'utilisation
image_path = "ressource\Perso_Mouvement.png"
save_path_horizontal = "ressource\Perso_Mouvement_inversee.png"


inverser_image_horizontal(image_path, save_path_horizontal)
