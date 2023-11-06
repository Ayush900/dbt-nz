from dbt.tests.adapter.constraints.test_constraints import (
    BaseConstraintsColumnsEqual,
    BaseTableConstraintsColumnsEqual,
    BaseViewConstraintsColumnsEqual,
    BaseIncrementalConstraintsColumnsEqual,
    BaseConstraintsRuntimeDdlEnforcement,
    BaseConstraintsRollback,
    BaseIncrementalConstraintsRuntimeDdlEnforcement,
    BaseIncrementalConstraintsRollback,
    BaseModelConstraintsRuntimeEnforcement,
    BaseConstraintQuotedColumn,
    BaseIncrementalContractSqlHeader,
    BaseTableContractSqlHeader,
    TestIncrementalForeignKeyConstraint as BaseIncrementalForeignKeyConstraint,
)

from dbt.tests.adapter.constraints.fixtures import (
    my_model_with_quoted_column_name_sql,
    my_model_incremental_wrong_order_sql,
    my_model_incremental_wrong_name_sql,
)
from tests.functional.adapter.constraint_fixtures import (
    model_quoted_column_schema_yml,
    test_constraint_quoted_column_netezza__expected_sql,
    model_schema_yml,
)
import pytest


class BaseConstraintsColumnsEqualNetezza(BaseConstraintsColumnsEqual):
    @pytest.fixture
    def string_type(self):
        return "VARCHAR(2000)"

class BaseIncrementalConstraintsColumnsEqualNetezza(BaseConstraintsColumnsEqual):
    @pytest.fixture(scope="class")
    def models(self):
        return {
            "my_model_wrong_order.sql": my_model_incremental_wrong_order_sql,
            "my_model_wrong_name.sql": my_model_incremental_wrong_name_sql,
            "constraints_schema.yml": model_schema_yml,
        }


class TestConstraintQuotedColumnNetezza(BaseConstraintQuotedColumn):
    @pytest.fixture(scope="class")
    def models(self):
        return {
            "my_model.sql": my_model_with_quoted_column_name_sql,
            "constraints_schema.yml": model_quoted_column_schema_yml,
        }

    @pytest.fixture(scope="class")
    def expected_sql(self):
            return test_constraint_quoted_column_netezza__expected_sql


class TestIncrementalConstraintsColumnsEqualNetezza(
    BaseIncrementalConstraintsColumnsEqualNetezza
):
    pass


class TestIncrementalConstraintsRollbackNetezza(BaseIncrementalConstraintsRollback):
    pass


class TestIncrementalConstraintsRuntimeDdlEnforcementNetezza(
    BaseIncrementalConstraintsRuntimeDdlEnforcement
):
    pass


class TestIncrementalContractSqlHeaderNetezza(BaseIncrementalContractSqlHeader):
    pass


class TestIncrementalForeignKeyConstraintNetezza(BaseIncrementalForeignKeyConstraint):
    pass


class TestModelConstraintsRuntimeEnforcementNetezza(
    BaseModelConstraintsRuntimeEnforcement
):
    pass


class TestTableConstraintsColumnsEqualNetezza(BaseTableConstraintsColumnsEqual):
    pass


class TestTableConstraintsRollbackNetezza(BaseConstraintsRollback):
    pass


class TestTableConstraintsRuntimeDdlEnforcementNetezza(
    BaseConstraintsRuntimeDdlEnforcement
):
    pass


class TestTableContractSqlHeaderNetezza(BaseTableContractSqlHeader):
    pass


class TestViewConstraintsColumnsEqualNetezza(BaseViewConstraintsColumnsEqual):
    pass
