"""seed profile_type values

Revision ID: seed_profile_type
Revises: create_profile_type
Create Date: 2025-01-21 00:00:00
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "seed_profile_type"
down_revision = "create_profile_type"
branch_labels = None
depends_on = None


def upgrade() -> None:
    connection = op.get_bind()
    result = connection.execute(sa.text("SELECT COUNT(1) FROM profile_type"))
    count = result.scalar() or 0
    if count:
        return

    profile_type_table = sa.table(
        "profile_type",
        sa.column("user_type", sa.String),
    )

    values = [
        {"user_type": "Médico(a)"},
        {"user_type": "Pediatra"},
        {"user_type": "Neuropediatra"},
        {"user_type": "Neurologista"},
        {"user_type": "Psiquiatra"},
        {"user_type": "Psiquiatra Infantil"},
        {"user_type": "Geneticista"},
        {"user_type": "Médico(a) de Família e Comunidade"},
        {"user_type": "Médico(a) do Desenvolvimento e Comportamento (quando disponível)"},
        {"user_type": "Gastroenterologista"},
        {"user_type": "Alergista/Imunologista"},
        {"user_type": "Otorrinolaringologista"},
        {"user_type": "Oftalmologista"},
        {"user_type": "Pneumologista"},
        {"user_type": "Endocrinologista"},
        {"user_type": "Dermatologista"},
        {"user_type": "Ortopedista"},
        {"user_type": "Médico(a) do Sono"},
        {"user_type": "Fisiatra (Medicina Física e Reabilitação)"},
        {"user_type": "Psicólogo(a)"},
        {"user_type": "Neuropsicólogo(a)"},
        {"user_type": "Psicoterapeuta"},
        {"user_type": "Analista do Comportamento (ABA)"},
        {"user_type": "Supervisor(a) ABA"},
        {"user_type": "Terapeuta ABA"},
        {"user_type": "Acompanhante Terapêutico(a) (AT)"},
        {"user_type": "Psicopedagogo(a)"},
        {"user_type": "Fonoaudiólogo(a)"},
        {"user_type": "Terapeuta Ocupacional"},
        {"user_type": "Fisioterapeuta"},
        {"user_type": "Psicomotricista"},
        {"user_type": "Terapeuta Psicomotor(a)"},
        {"user_type": "Educador(a) Físico(a)"},
        {"user_type": "Professor(a) de Educação Física Adaptada"},
        {"user_type": "Especialista em Comunicação Alternativa e Aumentativa (CAA)"},
        {"user_type": "Intérprete de Libras"},
        {"user_type": "Guia-intérprete (quando aplicável)"},
        {"user_type": "Nutricionista"},
        {"user_type": "Terapeuta Alimentar (seletividade/introdução alimentar - quando houver essa função no serviço)"},
        {"user_type": "Fonoaudiólogo(a) (disfagia/alimentação - quando aplicável)"},
        {"user_type": "Enfermeiro(a)"},
        {"user_type": "Técnico(a) de Enfermagem"},
        {"user_type": "Cirurgião(ã)-Dentista"},
        {"user_type": "Odontopediatra"},
        {"user_type": "Assistente Social"},
        {"user_type": "Professor(a)"},
        {"user_type": "Professor(a) Regente"},
        {"user_type": "Professor(a) de Educação Especial"},
        {"user_type": "Professor(a) do AEE (Atendimento Educacional Especializado)"},
        {"user_type": "Coordenador(a) Pedagógico(a)"},
        {"user_type": "Orientador(a) Educacional"},
        {"user_type": "Psicólogo(a) Escolar"},
        {"user_type": "Mediador(a) Escolar"},
        {"user_type": "Acompanhante Escolar"},
        {"user_type": "Cuidador(a) Escolar"},
        {"user_type": "Tutor(a) Escolar (quando usado pela instituição)"},
        {"user_type": "Professor(a) de Apoio"},
        {"user_type": "Musicoterapeuta"},
        {"user_type": "Arteterapeuta"},
        {"user_type": "Terapeuta de Integração Sensorial (especialização/ênfase em TO)"},
        {"user_type": "Equoterapeuta (quando praticado em programas específicos)"},
        {"user_type": "Terapeuta Assistido por Animais (quando existente no serviço)"},
        {"user_type": "Farmacêutico(a) (quando há acompanhamento de medicação)"},
        {"user_type": "Fonoaudiólogo(a) Educacional (quando aplicável)"},
        {"user_type": "Terapeuta Familiar (quando aplicável)"},
        {"user_type": "País"},
        {"user_type": "Responsável Legal"},
    ]

    op.bulk_insert(profile_type_table, values)


def downgrade() -> None:
    op.execute("DELETE FROM profile_type")
