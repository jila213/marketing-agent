def copywriting_prompt(product, target_group, goal):
    return f"""
    Erstelle einen überzeugenden Werbetext.

    Produkt: {product}
    Zielgruppe: {target_group}
    Marketingziel: {goal}

    Tonalität: kreativ, marketingorientiert
    """

def product_description_prompt(product, target_group):
    return f"""
    Erstelle eine professionelle Produktbeschreibung.

    Produkt: {product}
    Zielgruppe: {target_group}
    """

def campaign_idea_prompt(product, target_group, goal):
    return f"""
    Entwickle eine kreative Marketingkampagne.

    Produkt: {product}
    Zielgruppe: {target_group}
    Ziel: {goal}
    """
