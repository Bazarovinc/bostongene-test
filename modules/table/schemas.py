from pydantic import BaseModel, Field


class Signatures(BaseModel):
    mhci: float = Field(alias='MHCI')
    mhcii: float = Field(alias='MHCII')
    coactivation_molecules: float = Field(alias='Coactivation_molecules')
    effector_cells: float = Field(alias='Effector_cells')
    t_cell_traffic: float = Field(alias='T_cell_traffic')
    nk_cells: float = Field(alias='NK_cells')
    t_cells: float = Field(alias='T_cells')
    b_cells: float = Field(alias='B_cells')
    m1_signatures: float = Field(alias='M1_signatures')
    th1_signature: float = Field(alias='Th1_signature')
    antitumor_cytokines: float = Field(alias='Antitumor_cytokines')
    checkpoint_inhibition: float = Field(alias='Checkpoint_inhibition')
    treg: float = Field(alias='Treg')
    t_reg_traffic: float = Field(alias='T_reg_traffic')
    neutrophil_signature: float = Field(alias='Neutrophil_signature')
    granulocyte_traffic: float = Field(alias='Granulocyte_traffic')
    mdsc: float = Field(alias='MDSC')
    mdsc_traffic: float = Field(alias='MDSC_traffic')
    macrophages: float = Field(alias='Macrophages')
    macrophage_dc_traffic: float = Field(alias='Macrophage_DC_traffic')
    th2_signature: float = Field(alias='Th2_signature')
    protumor_cytokines: float = Field(alias='Protumor_cytokines')
    caf: float = Field(alias='CAF')
    matrix: float = Field(alias='Matrix')
    matrix_remodeling: float = Field(alias='Matrix_remodeling')
    angiogenesis: float = Field(alias='Angiogenesis')
    endothelium: float = Field(alias='Endothelium')
    proliferation_rate: float = Field(alias='Proliferation_rate')
    emt_signature: float = Field(alias='EMT_signature')
