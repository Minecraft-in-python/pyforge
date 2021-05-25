import minecraft.world.block as _block

Block = _block.Block
BlockColorizer = _block.BlockColorizer
get_block_icon = _block.get_block_icon

def register_block(s, block):
    _block.blocks.setdefault(s, block)
