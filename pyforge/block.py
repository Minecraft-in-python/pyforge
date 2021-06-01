import minecraft.block as _block
import minecraft.block.base as _block_base

Block = _block_base.Block
BlockColorizer = _block_base.BlockColorizer
get_block_icon = _block_base.get_block_icon

def register_block(s, block):
    _block.blocks.setdefault(s, block)
