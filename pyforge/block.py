import Minecraft.world.block as _block

Block = _block.Block
BlockColorizer = _block.BlockColorizer

def register_block(s, block):
    _block.blocks.setdefault(s, block)